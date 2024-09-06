```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to iterate through each string in the input list and checks if the `substring` is present in each string. If the `substring` is found in a string, that string is included in the resulting list and returned. If the `substring` is not found in any string, the resulting list will be empty. 

This approach ensures that the function is efficient and can efficiently handle large input lists and substrings.

The function is self-contained and easy to use, making it reusable for different input lists and substrings in the future. 

To verify the functionality, you can test it with different input lists and substrings to observe the expected behavior. Below are some example tests that you can execute to validate the function's correctness:
```python
# Test with an empty list
empty_list = []
substring = "abc"
result = filter_by_substring(empty_list, substring)
print(result)  # Output: []

# Test with a list containing one element
one_element_list = ["abc"]
substring = "abc"
result = filter_by_substring(one_element_list, substring)
print(result)  # Output: ['abc']

# Test with a list containing multiple elements
multi_element_list = ["abc", "bacd", "cde", "array"]
substring = "a"
result = filter_by_substring(multi_element_list, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```