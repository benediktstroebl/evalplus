Here's a Python script that implements the `filter_by_prefix` function:

```markdown
### Filter by Prefix Function
#### Description
Filter an input list of strings only for ones that start with a given prefix.

#### Usage
```python
from prefix_filter import filter_by_prefix

strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)

print(filtered_strings)  # Output: ['abc', 'array']
```

#### Code
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The list of strings to be filtered.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: The filtered list of strings.
    """
    # Use list comprehension to filter the input list
    return [string for string in strings if string.startswith(prefix)]

# Test cases
if __name__ == "__main__":
    # Test case 1: Empty input list
    print(filter_by_prefix([], 'a'))  # Output: []

    # Test case 2: Input list with strings having the prefix
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```

Note: The code is written to be concise and readable. The `filter_by_prefix` function uses list comprehension to filter the input list, which is a more Pythonic way to achieve this. The test cases are also included in the script to verify its correctness.