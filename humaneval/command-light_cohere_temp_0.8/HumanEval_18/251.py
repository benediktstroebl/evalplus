Here's the self-contained Python script with the function and tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns count of occurrences of substring in the given string.

    Args: 
        - string (str): string to search 
        - substring (sub): substring to search

    Returns: 
        - count (int): count of occurrences
    """
    return sum(1 for i, j in zip(string, substring) if j == string[i]))

# unit tests
def test_how_many_times():
    assert how_many_times("aaa", "aa") == 3
    assert how_many_times("abc", "a") == 2
    assert how_many_times("aaa", "a") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abcde", "abcd") == 3
    assert how_many_times(">", "a") == 0
```
This script defines a function how_many_times that counts the occurrences of a given substring in a given string. The function uses a Python generator expression along with the `zip` function to iterate over every combination of characters in the string and the substring, and checks if the corresponding characters are equal. 
The unit tests then validate the functionality of the function by testing different inputs.