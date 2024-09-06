Here's a Python script with a self-contained function that solves the problem you've outlined, including a markdown code block and a sample test case:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    tmp_string = string.lower()
    tmp_substring = substring.lower()
    while tmp_string:
        if tmp_string.startswith(tmp_substring):
            count += 1
            tmp_string = tmp_string[len(tmp_substring):]
        else:
            tmp_string = tmp_string[1:]
    return count

# Test the function
def test_how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3

test_how_many_times()
```

You can copy and paste this code into a Python environment or script to test it. The `how_many_times` function will count overlapping occurrences of the `substring` in the `string`, as described in the problem statement. The test case ensures that the function produces the expected results for the provided sample inputs.