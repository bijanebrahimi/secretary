# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import os
from unittest import TestCase, main
from secretary import Renderer
from secretary.utils import UndefinedSilently, pad_string


def test_undefined_silently():
    undefined = UndefinedSilently()

    assert isinstance(undefined(), UndefinedSilently)
    assert isinstance(undefined.attribute, UndefinedSilently)
    assert str(undefined) == ''


def test_pad_string():
    assert pad_string('TEST') == '0TEST'
    assert pad_string('TEST', 4) == 'TEST'
    assert pad_string(1) == '00001'


class MarkdownFilterTestCase(TestCase):
    def setUp(self):
        self.engine = Renderer(markdown_extras=['fenced-code-blocks'])
        self.engine.template_images = {}

    def test_paragraphs(self):
        test_samples = {
            'hello\n\n\nworld\n': 2,
            'hello world': 1,
        }
        pattern = r'<text:p text:style-name="Standard">[a-z ]+</text:p>'
        for test, occurances in test_samples.items():
            result = self.engine.markdown_filter(test)
            found = re.findall(pattern , result)
            assert len(found) == occurances

    def test_fenced_code_blocks(self):
        test = "```python\ndef test():\n    pass\n```"
        result = self.engine.markdown_filter(test)
        assert not 'python' in result

    def test_code_blocks(self):
        test = "```\ndef test():\n    pass\n```"
        result = self.engine.markdown_filter(test)
        assert 'codehilite' in result

    def test_code_blocks_indents(self):
        test_samples = {
            "```python\ndef test():\n    if True:\n        pass\n```": 3,
            "```\ndef test():\n    pass\n```": 1,
        }
        for test, occurances in test_samples.items():
            result = self.engine.markdown_filter(test)
            assert result.count('<text:tab/>') == occurances

    def test_new_line(self):
        test = "```python\ndef test():\n    pass\n```"
        result = self.engine.markdown_filter(test)
        assert not '\n' in result
