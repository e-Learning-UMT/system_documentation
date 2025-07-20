import datetime
import os
import sys
import time

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


sys.path.append(os.path.abspath(os.pardir))




with open("../pyproject.toml", "rb") as f:
    project_data = tomllib.load(f).get("project") or {}


# -- General configuration ----------------------------------------------------
templates_path = ["_templates"]
locale_dirs = ["locale/"]
gettext_compact = False
gettext_uuid = True
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinxext.opengraph",
]
source_suffix = ".rst"

# The master document must be in the project root so that index.html is built at
# the documentation's top level. Include ``source/index.rst`` from a short
# ``index.rst`` file at the root.
master_doc = "index"

project = project_data.get("name", "e-Learning Platrform Services Documentation").upper()
year = datetime.datetime.fromtimestamp(
    int(os.environ.get("SOURCE_DATE_EPOCH", time.time())), datetime.timezone.utc
).year
project_copyright = f"2010–{year}"  # noqa: RUF001
exclude_patterns = ["_build"]
release = project_data.get("version") or "1.0.0"
version = ".".join(release.split(".")[:1])
last_stable = release
requires_python = project_data.get("requires-python") or ""
min_python = requires_python.split(",")[0] if requires_python else "N/A"
rst_prolog = f"""
.. |last_stable| replace:: :pelican-doc:`{last_stable}`
.. |min_python| replace:: {min_python}
"""

extlinks = {"pelican-doc": ("https://docs.getpelican.com/en/latest/%s.html", "%s")}

# -- Options for HTML output --------------------------------------------------

html_theme = "furo"
html_title = "<strong>{project}</strong> <i>{release}</i>"
html_static_path = ["_static"]
html_theme_options = {
    "light_logo": "elearning.png",
    "dark_logo": "elearning.png",
    "navigation_with_keys": True,
}

# Output file base name for HTML help builder.
htmlhelp_basename = "Pelicandoc"

html_use_smartypants = True

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False


def setup(app):
    # overrides for wide tables in RTD theme
    app.add_css_file("theme_overrides.css")  # path relative to _static


# -- Options for LaTeX output -------------------------------------------------
# Use the same document name as ``master_doc`` for LaTeX outputs
latex_documents = [
    ("source/index", "Pelican.tex", "Pelican Documentation", "Justin Mayer", "manual"),
]

# -- Options for manual page output -------------------------------------------
man_pages = [
    ("source/index", "pelican", "pelican documentation", ["Justin Mayer"], 1),
    (
        "pelican-themes",
        "pelican-themes",
        "A theme manager for Pelican",
        ["Mickaël Raybaud"],
        1,
    ),
    (
        "themes",
        "pelican-theming",
        "How to create themes for Pelican",
        ["The Pelican contributors"],
        1,
    ),
]
