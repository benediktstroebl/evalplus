```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping matches.
    """
    how to use the function to find the number of occurrences of substring. 
    1. Returns: integer, `0` if substring is not found.
    """
    `string` could a string to search
    `substring` is the substring to find
    """
    return sum(1 for i, j in string.match(substring, string[i:j+1]))

# Unit Test
def test_how_many_times():
    assert how_many_times("aaa", "aa") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("aaaaaa", "aa") == 0
    assert how_many_times("abcde", "de") == 4

# Example usage
print(test_how_many_times())
 ```