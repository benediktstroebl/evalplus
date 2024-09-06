```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and including only those strings that contain the substring `substring`. This is specified by the conditional statement `if substring in s`. The expression `s in s` checks if the substring `substring` is present in the string `s`. 

The function's type hinting also indicates that it returns a list of strings as the output. This makes it easier for others to understand the function's purpose and the expected format of its output. Overall, the code is concise and clear in explaining its functionality. 

The unit tests for this function are straightforward since we can use the `assertIn` function to check if a certain string contains a substring. 

For example: 
```python
def test_filter_by_substring():
    # Test case 1: Empty input list, substring 'a'
    input_list = []
    substring = 'a'
    expected_output = []
    assert filter_by_substring(input_list, substring) == expected_output

    # Test case 2: List with one element, substring 'a'
    input_list = ['abc']
    substring = 'a'
    expected_output = ['abc']
    assert filter_by_substring(input_list, substring) == expected_output

    # Test case 3: List with multiple elements, substring 'a'
    input_list = ['abc', 'bacd', 'cde', 'array']
    substring = 'a'
    expected_output = ['abc', 'bacd', 'array']
    assert filter_by_substring(input_list, substring) == expected_output

    # Test case 4: Empty input list, substring ''
    input_list = []
    substring = ''
    expected_output = []
    assert filter_by_substring(input_list, substring) == expected_output

    # Test case 5: List with whitespace characters only
    input_list = ['  ', '   ', '    ', '  \n  ', '   \t']
    substring = ' '
    expected_output = ['  ', '   ', '    ', '  \n  ', '   \t']
    assert filter_by_substring(input_list, substring) == expected_output
```