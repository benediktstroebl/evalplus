```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    Count overlapping matches.

    Example count = 0
    str.findall(substring, string)
    count+=1
    for i in range(len(string) - len(substring)):
        count+=str.findall(substring, string[i:])
    return count
    """

# Test cases for how_many_times() function
def test_how_many_times():
    assert how_many_times("aaa", "aa") == 3
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abcde", "abc") == 2
    assert how_many_times("abcba", "abc") == 2
    assert how_many_times("abcdeabc", "abc") == 3
    assert how_many_times("aaa", "aa") == 0
    assert how_many_times("aaaaaa", "aaaa") == 0
```
This code defines a function called **how_many_times()** that returns the count of how many times a given substring can be found in the original string. 

The function uses the **str.findall()** function with the substring as the search string and the original string as the collection of substrings, and the **count** variable is incremented for each match found. The function then checks the strings that have the same substring and returns the total count of matches.