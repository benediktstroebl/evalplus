```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to filter
    substring (str): The substring to search for

    Returns:
    List[str]: The filtered list of strings
    """
    # Initialize an empty list to store the filtered strings
    filtered_strings = []

    # Iterate over each string in the input list
    for string in strings:
        # Check if the substring is present in the current string
        if substring in string:
            # If the substring is found, add the string to the filtered list
            filtered_strings.append(string)

    # Return the filtered list of strings
    return filtered_strings


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Expected: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected: ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. The function uses a simple loop to iterate over the input list and appends each string to the filtered list if the substring is found in it. The test cases are included at the end of the script to demonstrate its usage and verify its correctness.