```python
def strlen(string: str) -> int:
    """ Returns the length of a string """
    return len(string)
```
```python
from unittest.mock import patch, call
import unittest

class TestStringLength(unittest.TestCase):
    @patch('builtins.len')
    def test_strlen_returns_int_for_empty_string(self, mock_len):
        strlen('')
        mock_len.assert_called_once_with('')

    @patch('builtins.len')
    def test_strlen_returns_int_for_non_empty_string(self, mock_len):
        strlen('abc')
        mock_len.assert_called_once_with('abc')
```