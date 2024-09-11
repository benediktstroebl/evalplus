```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): Input string

    Returns:
    List[str]: List of prefixes

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
    print(all_prefixes('python'))  # Output: ['p', 'py', 'pyt', 'pyth', 'pytho', 'python']
```