```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of prefixes from shortest to longest.
    """
    return [string[:i] for i in range(1, len(string) + 1)]


# Example usage
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```