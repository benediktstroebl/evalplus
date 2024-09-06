Here's a Python function that solves the problem of finding the number of times a substring occurs within a given string. The function also accounts for overlapping instances of the substring:
```python
def how_many_times(string, substring):
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    n = len(string)
    m = len(substring)
    count = 0
    idx = 0
    while idx < n - m + 1:
        if string[idx:idx+m] == substring:
            count += 1
            idx += 1
        else:
            idx += 1
        # To handle overlapping cases, we don't increment idx here, and continue searching in the remainder of the loop.
    return count

# Unit tests:
def test_empty_string():
    assert how_many_times('', 'a') == 0

def test_same_string():
    assert how_many_times('aaa', 'a') == 3

def test_overlapping_count():
    assert how_many_times('aaaa', 'aa') == 3

def test_subsequent_occurrences():
    assert how_many_times('abcdabcd', 'abcd') == 2

test_empty_string()
test_same_string()
test_overlapping_count()
test_subsequent_occurrences()
```

This script defines the `how_many_times` function and includes unit tests to verify its correctness against various test cases. Simply copy and paste this code into a Python environment or script to use and test the function.  Please note that the function's explanation and test cases provided earlier are still applicable to this script. This code simply encapsulates the function and incorporates tests in a self-contained manner.