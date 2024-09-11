```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to filter
    substring (str): A substring to search for in each string

    Returns:
    List[str]: A filtered list of strings containing the given substring
    """
    # Use list comprehension to create a new list that includes strings containing the substring
    return [string for string in strings if substring in string]

# Test cases
if __name__ == '__main__':
    test_cases = [
        (["", "", ""], ""),
        (["abc", "bacd", "cde", "array"], "a"),
        (["hello", "world", "python"], "o"),
        ([], "a"),
        (["abc", "bacd", "cde"], "x")
    ]

    for strings, substring in test_cases:
        try:
            result = filter_by_substring(strings, substring)
            print(f"Input: strings={strings}, substring='{substring}'")
            print(f"Expected: [{''.join(strings)}] (no match in empty string)")
            print(f"Result: {result}")
            print()
        except Exception as e:
            print(f"Error: {str(e)}\n")
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings from the input list that include the specified substring. It also includes test cases to verify the function's correctness.