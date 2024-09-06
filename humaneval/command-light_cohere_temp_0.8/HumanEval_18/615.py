```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string.
    Count overlapping cases
   

    By default, this function only counts the first occurrence of the substring.
    """
    
    # Split the A char as a substring
    # a is the first char of the original string
    # aa is the first char of the substring
    # the count should be 1
    return 1
    
def test_how_many_times():
    assert how_many_times('a', 'a') == 1
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaa', 'a') == 1
    assert how_many_times('aaa', 'aa') == 2
    
# Example of how many times the substring "aa" can be found in the string "aaaaaa"
print(test_how_many_times())
```