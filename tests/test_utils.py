import pytest
from gitignore_cli.utils import list_available_templates


@pytest.fixture
def mock_templates_dir(tmpdir):
    """Fixture to create a mock templates directory with .gitignore files."""
    templates_dir = tmpdir.mkdir("templates")

    # Cria alguns arquivos .gitignore de exemplo fora de ordem alfabética
    templates_dir.join("Python.gitignore").write("# Python template content")
    templates_dir.join("Java.gitignore").write("# Java template content")
    templates_dir.join("Node.gitignore").write("# Node template content")

    return templates_dir


def test_list_available_templates_sorted(mock_templates_dir, monkeypatch):
    """Test if list_available_templates returns templates in alphabetical order."""
    # Força a função a usar o diretório de templates simulado
    monkeypatch.setattr('os.path.dirname', lambda _: str(mock_templates_dir))

    # Chama a função e verifica se a lista está ordenada
    templates = list_available_templates(str(mock_templates_dir))

    # Verifica se a lista está em ordem alfabética
    assert templates == sorted(templates), "The templates should be in alphabetical order"
