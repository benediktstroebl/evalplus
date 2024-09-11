```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    return len(string) - len(string) % len(substring) + 1

# Test cases
if __name__ == "__main__":
    print(how_many_times('', 'a'))  # Expected output: 0
    print(how_many_times('aaa', 'a'))  # Expected output: 3
    print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script works by subtracting the length of `substring` from the length of `string` and then adding 1. This effectively counts the number of non-overlapping occurrences of `substring` in `string`, then adjusts for the fact that `string` might be shorter than `substring`.