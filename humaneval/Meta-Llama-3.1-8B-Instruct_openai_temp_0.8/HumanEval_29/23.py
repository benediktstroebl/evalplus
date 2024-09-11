```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of input strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    return [s for s in strings if s.startswith(prefix)]

# Test the function
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Expected output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to achieve this.

The `startswith` method of the string class is used to check if each string in the input list starts with the given prefix. The list comprehension iterates over the input list, applies the condition to each string, and includes the string in the output list if the condition is true.

The script also includes two test cases to verify the correctness of the function. The first test case checks that an empty list is returned when the input list is empty. The second test case checks that the correct strings are returned when the input list contains multiple strings.