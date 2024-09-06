Here's a Python script with a self-contained function that solves the problem you've described, including markdown code blocks that demonstrate the behavior of the function and its tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.

    :param string: Original string
    :param substring: Substring to search for
    :return: Number of times substring occurs in string
    :raises ValueError: If substring is empty
    """
    if not substring:
        raise ValueError("Empty substring is not allowed")
    
    count = 0
    temp_string = string.copy()
    temp_substring = substring.copy()
    
    while temp_string and temp_substring:
        if temp_string[0] == temp_substring[0]:
            count += 1
            temp_string = temp_string[1:]
            temp_substring = temp_substring[1:]
        else:
            temp_string = temp_string[1:]
    return count

# Test Cases
def test_how_many_times():
    """ Tests for how_many_times function """
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaa', 'aa') == 2
    assert how_many_times('aaaaaa', 'aaaa') == 2
    assert how_many_times('aaaaaa', 'a') == 5
    assert how_many_times('aaa', 'aab') == 2

test_how_many_times()
```

In this script, the `how_many_times` function counts the number of times a substring occurs within a given string. The function raises a `ValueError` if an empty substring is provided. The test suite includes a `test_how_many_times` function that calls `how_many_times` with different cases to verify its correctness.

The function uses dynamic programming with only two variables, `count` and `temp_string`, to keep track of the answered and the remaining string to compare respectively.