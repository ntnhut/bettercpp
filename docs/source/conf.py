# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Better C++'
copyright = '2024, Nhut Nguyen'
author = 'Nhut Nguyen'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

master_doc = 'index'

# -- Options for HTML output

html_theme = 'furo'
html_title = 'Better C++'
# html_logo = "nhut_transparent.png"
html_theme_options = {
    # 'logo_only': True,
    # "sidebar_hide_name": True,
    # 'nosidebar': True,
    # "announcement": "Support my work by buying my books <a href='https://store.nhutnguyen.com'  target='_blank'>here</a>!", 
}


latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',
    'sphinxsetup': 'hmargin={1.2in,1.2in}, vmargin={1.2in,1.2in}',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
                    \usepackage{charter}
                    \usepackage[defaultsans]{lato}
                    \usepackage{inconsolata}
                    \addto\captionsenglish{\renewcommand{\contentsname}{Contents}}
                ''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',        
}
latex_show_urls = 'footnote'
# latex_documents = [
#     (master_doc, 'leetsolve.tex', 'Better C++',
#      'Nhut Nguyen, Ph. D.', 'book'),
# ]
latex_docclass = {
   'book': 'book',
}
# -- Options for EPUB output
# epub_show_urls = 'footnote'