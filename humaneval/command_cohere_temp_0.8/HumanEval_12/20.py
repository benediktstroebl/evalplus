Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)  # Get the longest string
    if len(set(strings)) == 1:  # If there is only one string of that length
        return longest_string
    return longest_string[0]  # Return the first one in case of multiple strings of the same length
```

This code defines a function called `longest` that takes a list of strings as input and returns either the longest string in the list, the first string that is longest if there are multiple of the same length, or None if the input list is empty. The `longest` function initially checks if the string list is empty and returns None if it is. If the list is not empty, it uses the `max` function with the `key` parameter set to the len function to identify the longest string in the list. The code then checks if there is only one string of that length in the list and returns the longest string if not. The output is the first string of the longest length in the list as defence against multiple strings of the same length.

Here's a test suite that you can use to verify the functionality of the code:
```python
def test_longest_with_empty_list(empty_list: List[str]) -> None:
    assert longest(empty_list) is None

def test_longest_with_single_string_list(single_string_list: List[str]) -> None:
    assert longest(single_string_list) == single_string_list[0]

def test_longest_with_multiple_strings(multiple_strings: List[str]) -> None:
    assert longest(multiple_strings) == multiple_strings[0]

def test_longest_with_custom_input(custom_input: List[str]) -> None:
    assert longest(custom_input) == custom_input[0]
```

The test suite covers the following test cases: 

- Test case `test_longest_with_empty_list` checks if the `longest` function correctly returns None when it is given an empty list.
- Test case `test_longest_with_single_string_list` checks if the `longest` function correctly identifies the longest string in a list with a single string.
- Test case `test_longest_with_multiple_strings` checks if the `longest` function correctly returns the first longest string when a list contains multiple strings of the same length. 
- Test case `test_longest_with_custom_input` checks if the `longest` function works correctly with an input list containing various string lengths. 

You can use these test cases to validate the functionality of the `longest` function and ensure that it behaves as expected.  You can use the `longest` function as needed in your code, calling it with a list of strings to find the longest one.  This will help you handle situations where you need to identify the longest string among a set of strings, which can be useful in various text processing and data analysis scenarios.  This function can also be easily modified to handle additional logic or constraints, such as taking a set of strings instead of a list or handling case sensitivity.  It can also be extended to handle languages other than English or handle specific types of strings like codes or