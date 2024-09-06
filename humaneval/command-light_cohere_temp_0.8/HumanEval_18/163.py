```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string, 
    including overlapping occurrences.
    Args: 
        string (str): The original string
        substring (str): The substring to find
    Returns: 
        int: Number of occurrences
    """
    occurrences = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            occurrences += 1
    return occurrences

# Unit tests
def test_how_many_times():
    assert how_many_times('aaaa', 'aa') == 3
 assert how_many_times('hello', 'o') == 0
 assert how_many_times('hello', 'll') == 0
 assert how_many_times('abcde', 'abcde') == 2
 assert how_many_times('abcba', 'abc') == 3
```
The function, `how_many_times`, finds the number of occurrences of a given substring in a given string. The function iterates over the strings using a for loop and counts the occurrences.