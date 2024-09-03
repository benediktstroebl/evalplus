```python
def is_happy(s):
    """Check if the string is happy.

    Args:
        s (str): Input string.

    Returns:
        bool: True if string is happy, False otherwise. Happy string has length at least 3 and every 3 consecutive letters are distinct.
    """
    return len(s) >= 3 and all(s[i] != s[i + 1] != s[i + 2] for i in range(len(s) - 2))
```