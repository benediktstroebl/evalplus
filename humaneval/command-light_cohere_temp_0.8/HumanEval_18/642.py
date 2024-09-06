```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string.
    Count overlapping matches.
    Returns a specific implementation for a case where the substring can be of any length.
    """
    find_times: iterates through the original string and counts the occurrences of each prefix of the substring.
    Return the total number of occurrences of the substring.
    """
find_times = [substring] + [string[i:]] for i in range(len(substring))
    return len(find_times)

# Unit tests
def test_how_many_times():
    assert how_many_times('aaa', 'aa') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'abcd') == 5
    assert how_many_times('getsup', 'get') == 1
    assert how_many_times('abcba', 'ab') == 2
    assert how_many_times('abc', 'a') == 0
    assert how_many_times('abc', 'ab') == 1
    assert how_many_times('', '') == 0
```
The function `how_many_times` in the code above accepts two arguments: a string and a substring. It creates a the function to identify the frequency of a given substring in the string. The code also provides a unit tests for the `how_many_times` function to ensure its functionality.