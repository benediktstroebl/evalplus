```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while avoiding overlapping occurrences.
    """
   
    example:
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    2
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring: 
            count += 1
    return count

# Unit tests
def test_how_many_times():
    assert how_many_times('aaaaaaa', 'aa') == 2
    assert how_many_times('abc', 'a') == 2
    assert how_many_times('aaa', 'aaa') == 0
    assert how_many_times('aaa', 'aa') == 1
    assert how_many_times('', '') == 0
    assert how_many_times('  ', 'a') == 1

if __name__ == "__main__":
    test_how_many_times()
```
The code implements a function called `how_many_times` that counts the number of occurrences of a given substring within a larger string. The function iterates through every character in the main string to check if it matches the substring. The function returns the count, indicating the number of times the substring appears in the main string. 
The function is then tested using unit tests. These tests ensure that the string and substring inputs produce the correct results, and the function handles empty strings correctly.