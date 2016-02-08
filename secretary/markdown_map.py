#!/usr/bin/python
try:
    from collections import OrderedDict
except:
    # Python 2.6 backward compatibility
    from ordereddict import OrderedDict

from .utils import list_id


# Transform map used by the markdown filter. transform_map have
# instructions of how to transform a HTML style tag into a ODT document
# styled tag. Some ODT tags may need extra attributes; these are defined
# as a dict in the 'style_attributes' key. Also, some tags may need to create
# new styles in the document.

common_styles = {
	'italic': {
        'replace_with': 'text:span',
        'style_attributes': {
            'style-name': 'markdown_italic'
        },

        'style': {
            'name': 'markdown_italic',
            'properties': {
                'fo:font-style': 'italic',
                'style:font-style-asian': 'italic',
                'style:font-style-complex': 'italic'
            }
        }
    },
    'strong': {
        'replace_with': 'text:span',
        'style_attributes': {
            'style-name': 'markdown_bold'
        },

        'style': {
            'name': 'markdown_bold',
            'properties': {
                'fo:font-weight': 'bold',
                'style:font-weight-asian': 'bold',
                'style:font-weight-complex': 'bold'
            }
        }
    }
}

transform_map = OrderedDict([
    # Links
    ('a', {
		'replace_with': 'text:a',
		'attributes': {
			'xlink:type': 'simple',
			'xlink:href': ''
		}),

    # Paragraphs
    ('p', {
        'replace_with': 'text:p',
        'style_attributes': {
            'style-name': 'Standard'
        }),


    # Texts
    ('strong', common_styles['strong']),
    ('b', common_styles['strong']),
    ('em', common_styles['italic']),
    ('i', common_styles['italic']),

    # Headings
    ('h1', {
        'replace_with': 'text:p',
        'style_attributes': {
            'style-name': 'Heading_20_1'
        }
    }),
    ('h2', {
        'replace_with': 'text:p',
        'style_attributes': {
            'style-name': 'Heading_20_2'
        }
    }),
    ('h3', {
        'replace_with': 'text:p',
        'style_attributes': {
            'style-name': 'Heading_20_3'
        }
    }),
    ('h4', {
        'replace_with': 'text:p',
        'style_attributes': {
            'style-name': 'Heading_20_4'
        }
    }),
    ('h5', {
        'replace_with': 'text:p',
        'style_attributes': {
            'style-name': 'Heading_20_5'
        }
    }),
    ('h6', {
        'replace_with': 'text:p',
        'style_attributes': {
            'style-name': 'Heading_20_6'
        }
    }),

    # Codes
    ('pre', {
        'replace_with': 'text:p',
        'style_attributes': {
            'style-name': 'Preformatted_20_Text'
        }
    }),
    ('code', {
        'replace_with': 'text:p',
        'style_attributes': {
            'style-name': 'Preformatted_20_Text'
        }
    }),

    # Lists
    ('ul', {
        'replace_with': 'text:list',
        'attributes': {
            'xml:id': list_id()
        }
    }),
    ('ol', {
        'replace_with': 'text:list',
        'attributes': {
            'xml:id': list_id()
        }
    }),

    # Items
    ('li', {
        'replace_with': 'text:list-item'
    })
])
