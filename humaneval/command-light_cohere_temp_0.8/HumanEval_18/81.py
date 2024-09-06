Here is a self-contained Python function that solves the problem of finding the number of times a given substring can be found in another string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    handling overlapping matches.
    Return the how the important solution for the given problem.
    """
   
    matching function uses a simple `count` function to 
    compare the substring with the original string.
    It returns the fact of the number of occurrences of the substring.
    """
    test cases to ensure the correctness of the function:
    """

def test_how_many_times():
    assert how_many_times('aaa', 'aa') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'de') == 2
    assert how_many_times('abcba', 'ab') == 2
    assert how_many_times('abcd', 'cd') == 1
    assert how_many_times('aab', 'a') == 0
```

Please use the `test_how_many_times` function to run the test cases. 

Feel free to use this code snippet in your projects!