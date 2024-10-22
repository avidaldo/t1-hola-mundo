import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestHelloWorld(unittest.TestCase):
    @patch('builtins.input', return_value='John')
    @patch('sys.stdout', new_callable=StringIO)
    def test_hello_name(self, mock_stdout, mock_input):
        main.hello_name()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Hello, John!')

if __name__ == '__main__':
    unittest.main()
