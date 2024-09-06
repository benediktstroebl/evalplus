```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test suite to verify the function
def test_how_many_times():
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abc", "a") == 2
    assert how_many_times("abcde", "abc") == 3
    assert how_many_times("abcde", "ab") == 2
    assert how_many_times("XYZ123", "X") == 3
    assert how_many_times("ABC123", "ABC") == 2
    assert how_many_times("abc", "") == 0
```  The provided Python script defines a function called **how_many_times()** that aims to determine the frequency of a given substring within a given string. The function utilizes a string's characters as a counter to tally the occurrences of the substring.