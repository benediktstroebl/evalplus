```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    # Use list comprehension to generate all prefixes of the string
    # The range starts from 1 to include the single character prefix and ends at the length of the string + 1 to include the whole string as the longest prefix
    return [string[:i] for i in range(1, len(string) + 1)]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']

# Test the function
def main():
    """
    Test the all_prefixes function with assertions.
    """
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcdef') == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
    assert all_prefixes('a') == ['a']
    assert all_prefixes('') == []

if __name__ == "__main__":
    main()
```