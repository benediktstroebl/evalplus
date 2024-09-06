```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that begin with the input prefix. The function uses a list comprehension, which is a concise way to create lists in Python.

The basic syntax for the list comprehension is:
```python
return_list = [expression for item in sequence if condition]
```

This Python script solves the problem of filtering a list of strings based on a prefix using a self-contained function, and its behavior is defined by its parameters.  By using the `startswith` method, the script efficiently checks whether each string in the list begins with the provided prefix or not. The resulting filtered list is then returned.  This approach proves pragmatic, as it forgoes the need for additional helper functions or recursive calls, thus ensuring brevity and clarity.

This function can be easily tested. For example, to test the function with a sample input, you can use the following code:
```python
# Test the function with a sample input
input_strings = ['abc', 'bcd', 'cde', 'array']
input_prefix = 'a'
expected_output = ['abc', 'array']

result = filter_by_prefix(input_strings, input_prefix)
assert result == expected_output
```

This test verifies if the `filter_by_prefix` function correctly returns the anticipated results when provided custom inputs. The assert statement checks if the computed `result` equals the `expected_output`, which ought to be true due to the function's proper functionality.  Thus, the test passes.