Here's a Python function that solves the problem of finding the number of times a substring occurs in a given string. The function also accounts for overlapping instances of the substring:
```python
def how_many_times(string, substring):
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.
    
    Args:
        string (str): Original string.
        substring (str): Substring to search for.
    
    Returns:
        int: Number of occurrences of the substring in the original string.
    """
    if not string or not substring:
        return 0
    
    count = 0
    n = len(string)
    m = len(substring)
    
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            count += 1
    
    return count
```

This function takes two strings as input and returns the number of times the substring occurs in the original string, including overlapping instances. It uses a loop to compare the substring to sequential parts of the original string and increments the count if there's a match. The empty string and empty substring cases are handled, and the function returns 0 in such cases. 

The function is straightforward and efficiently solves the problem statement without requiring any external libraries. Test cases can be added to ensure its correctness. 
```python
# Test the how_many_times function
def test_how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    
    assert how_many_times('abcabcab', 'abc') == 3
    assert how_many_times('abc', 'abc') == 1
    assert how_many_times('abc', 'ac') == 0
    assert how_many_times('ab', 'ab') == 2
    assert how_many_times('aaa', 'aaa') == 3
    assert how_many_times('aaaaaaa', 'aaaa') == 4

test_how_many_times()
``` 
This test suite includes various scenarios to validate the function's behavior.