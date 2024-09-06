```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string Count overlapping cases."""
    
    # Count the occurrences of substring in the string
    return sum(1 for i in string.find(substring, re. how) or constant substring is how to test.
    return 0
specific cases:
    assert how_many_times('', 'a') == 0, "empty string"
    assert how_many_times('aaaa', 'a') == 3, "Should get 3 for 'aaaaaa'"
    assert how_many_times('abcdeabcde', 'abcde') == 3, "Should get 3 for 'abcdeabcdeabcde'"
    assert how_many_times('aaa', 'aa') == 3, "Should get 3 for 'aaaaaa'"
    assert how_many_times('abcd', 'ab') == 2, "Should get 2 for 'abcdab'"
    assert how_many_times('abcdefgh', 'def') == 4, "Should get 4 for 'abcdefghdef'"
    return 

```