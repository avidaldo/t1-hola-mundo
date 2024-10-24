import pytest
from io import StringIO
import sys
import os

# Ensure the parent directory (containing main.py) is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main  # Import the main module


# Test function using pytest's monkeypatch for mocking input
def test_hello_name(monkeypatch, capsys):
    # Mock input to return 'John'
    monkeypatch.setattr('builtins.input', lambda _: 'John')

    # Call the function
    main.hello_name()

    # Capture the output
    captured = capsys.readouterr()

    # Check the expected output
    assert captured.out.strip() == 'Hello, John!'
