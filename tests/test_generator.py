import os
import pytest
from gitignore_cli.generator import generate_gitignore


@pytest.fixture
def temp_gitignore_file(tmpdir):
    """Fixture to create a temporary .gitignore file for testing."""
    return tmpdir.join(".gitignore")


def test_generate_single_template(temp_gitignore_file):
    """Test generating a .gitignore file with a single template."""
    generate_gitignore(['Python'], str(temp_gitignore_file), no_header=True)

    # Check if the file was generated
    assert os.path.isfile(str(temp_gitignore_file))

    # Read the content of the generated file
    with open(str(temp_gitignore_file), 'r') as f:
        content = f.read()

    # Assert that the content contains relevant data from the Python template
    assert 'Python' in content


def test_generate_multiple_templates(temp_gitignore_file):
    """Test generating a .gitignore file with multiple templates."""
    generate_gitignore(['Python', 'Node'], str(temp_gitignore_file), no_header=True)

    # Read the content of the generated file
    with open(str(temp_gitignore_file), 'r') as f:
        content = f.read()

    # Assert that the content contains both Python and Node sections
    assert 'Python' in content
    assert 'Node' in content


def test_generate_with_header(temp_gitignore_file):
    """Test generating a .gitignore file with a custom header."""
    generate_gitignore(['Python'], str(temp_gitignore_file), no_header=False)

    # Read the content of the generated file
    with open(str(temp_gitignore_file), 'r') as f:
        content = f.read()

    # Check for the presence of the custom header
    assert 'generated by gitignore-cli' in content
    assert 'Python' in content