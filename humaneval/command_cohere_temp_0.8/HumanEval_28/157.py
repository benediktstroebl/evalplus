```python
# Importing the necessary module
from typing import List

# The function to be defined and solved
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result

# Unit tests
import unittest

class TestConcatenate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_list_with_elements(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()
```

Let's break down the code step by step:
1. **Importing Module**: The `from typing import List` line imports the `List` module from the `typing` module. This allows you to define the type of the function argument and return value.
2. **Function Definition**: The `def concatenate(strings: List[str]) -> str:` line defines the `concatenate` function. It takes a single argument `strings`, which is a list of strings, and returns a single string.
3. **Empty List Handling**: The function body consists of a loop that iterates over each string in the input list. It appends each string to the `result` variable, which is initially set to an empty string. This action effectively concatenates the strings.
4. **Unit Tests**: The code then imports the `unittest` module and defines a test class `TestConcatenate` that inherits from `unittest.TestCase`. This class contains two test methods, each representing a specific test:
    - `test_empty_list`: This test checks if the `concatenate` function correctly handles an empty list, ensuring that it returns an empty string.
    - `test_list_with_elements`: This test checks if the `concatenate` function correctly concatenates a list of strings, expecting 'abc' when passed the list ['a', 'b', 'c'].
5. **Execution of Tests**: The `if __name__ == '__main__':` block ensures that the test cases are executed only when the script is run directly (not imported as a module). It calls `unittest.main()` to run all the test methods in the `TestConcatenate` class.

The script shows how to define a function, encapsulate it with a meaningful docstring, and then validate its behavior with unit tests. The tests ensure that the function behaves as expected even in edge cases, such as an empty list or a list with elements.