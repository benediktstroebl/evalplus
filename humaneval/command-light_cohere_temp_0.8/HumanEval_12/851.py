```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    # Check if empty input
    if not strings:
        return None
    # Sort the strings alphabetically
    strings.sort(str) = sorted(strings, key=str.find)
    longest_str = strings[0]
    # Return the length of the longest string
    return [len(longest_str)]

# Test cases
test_ longest = [
    ["a", "b", "c"],
    ["a", "bb", "ccc"],
    ["aa", "bb", "ccc"],
    ["aa", "bb", "bbb", "ccc"]
]

# Call the function and assert the result is correct
print(f'Longest string: {test_longest}')
print(f'Length: {longest([test_longest]))}')
```