# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus

# this package
from seed_intersphinx_mapping.requirements_parsers import parse_requirements_txt

example_requirements_a = """\
domdf_python_tools>=0.4.8
packaging>=20.4
requests>=2.24.0
slumber>=0.7.1
sphinx>=3.0.3
"""

expected_requirements_a = [
		"domdf_python_tools",
		"packaging",
		"requests",
		"slumber",
		"sphinx",
		]

bad_example_requirements = """\
domdf_python_tools>=0.4.8
packaging>=20.4
?==requests>=2.24.0
slumber$$$$0.7.1
sphinx>=3.0.3
"""

bad_expected_requirements = [
		"domdf_python_tools",
		"packaging",
		"sphinx",
		]


@pytest.mark.parametrize(
		"contents, expects", [
				(example_requirements_a, expected_requirements_a),
				(bad_example_requirements, bad_expected_requirements),
				]
		)
def test_parse_requirements_txt(tmpdir, contents, expects):
	(PathPlus(tmpdir) / "requirements.txt").write_text(contents)

	assert parse_requirements_txt(tmpdir) == expects
