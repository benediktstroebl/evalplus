```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring within the original string, 
    including overlapping substring matches.

    Args:
        string: The input string
        substring: The substring to search for

    Returns:
    int: The number of times the substring appears in the string
    """
    return sum(1 for x in string.over.find(substring, lambda s: s in string))

def test_function_pass():
    assert how_many_times("aaaa", "aa") == 3
```