```python
# Importing the necessary module
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result

# Tests
def test_empty_list():
    assert concatenate([]) == ''

def test_non_empty_list():
    assert concatenate(['a', 'b', 'c']) == 'abc'

if __name__ == '__main__':
    test_empty_list()
    test_non_empty_list()
```

This script includes the `concatenate` function and automated tests for the function using the `test_empty_list` and `test_non_empty_list` functions to ensure its correctness against different test cases. When executed directly, the script will run the tests and display the results. 
The function `concatenate` takes a list of strings as input and returns a single string that concatenates all the strings in the list separated by their default separator, the blank space. 
The `test_empty_list` function tests the function `concatenate` with an empty list as an argument and asserts that the result is an empty string. 
The `test_non_empty_list` function tests the function `concatenate` with a list that contains one element and asserts that the result is the same as the element in the list. 
Since the code is enclosed within the `if __name__ == '__main__':` block, the tests will only be executed when the script is run directly and not when it's imported as a module. 
To run the tests, simply run the script. If the tests pass, you should see output indicating that the tests were successful. If there's an assertion error, it will be indicated with an appropriate error message.