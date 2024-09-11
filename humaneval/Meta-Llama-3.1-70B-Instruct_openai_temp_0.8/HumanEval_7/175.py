```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to be filtered
        substring (str): A substring to filter by

    Returns:
        List[str]: A list of strings containing the given substring
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

if __name__ == "__main__":
    print("All test cases passed!")
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. It uses a list comprehension to create the new list, and the `in` operator to check if the substring is present in each string.

The script also includes two test cases to verify the correctness of the function, using the `assert` statement. If the function passes all the test cases, it prints "All test cases passed!".