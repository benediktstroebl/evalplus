```markdown
### Problem Solution: All Prefixes of a String

This Python script generates a list of all prefixes from shortest to longest of a given input string.

#### Script
```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    :param string: Input string
    :return: List of all prefixes
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

#### Explanation

*   We create an empty list `prefixes` to store all prefixes.
*   We iterate over the range from 1 to the length of the input string (inclusive).
*   For each index `i`, we append a prefix of the input string to the `prefixes` list using `string[:i]`, which returns a substring from the start of the string to the `i-th` character.
*   Finally, we return the list of all prefixes.

This solution has a time complexity of O(n^2) due to the substring operations, but it is simple and easy to understand. If performance is a concern for large input strings, a more efficient approach could be implemented using a loop to generate the prefixes.