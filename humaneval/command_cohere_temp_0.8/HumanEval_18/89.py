Here's a Python function that solves the problem of finding the number of times a substring occurs in a given string. The function handles overlapping cases as described in the prompt. The function is also accompanied by a test suite to ensure its correctness:
```python
def how_many_times(string: str, substring: str) -> int:
    """Find how many times a given substring can be found in the original string. Count overlaping cases."""
    if not string or not substring:
        return 0
    
    num_occurrences = 0
    
    # Using a loop to find occurrences for efficiency and to handle overlapping cases
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            num_occurrences += 1
    
    return num_occurrences

# Tests
def test_how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaa', 'aaa') == 1
    assert how_many_times('aaaaaa', 'aaaa') == 2
    assert how_many_times('abcabcabc', 'abc') == 3

if __name__ == "__main__":
    test_how_many_times()
```

In this script, the `how_many_times` function iterates through each substring starting at each character of the input string. It checks if the substring matches the given substring, and if it does, it increments the `num_occurrences` counter. The test suite covers various edge cases to ensure the function works correctly.