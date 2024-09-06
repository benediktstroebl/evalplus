Here's a Python script with a self-contained function that solves the problem you've outlined, including tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    for i in range(len(string)-len(substring)+1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

# Tests
def test_how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('aaab', 'aa') == 2
    assert how_many_times('aaaa', 'aaa') == 1
    assert how_many_times('aaaa', 'aaaa') == 1

if __name__ == "__main__":
    test_how_many_times()
```
This script includes a test suite with one defined test case, and the `how_many_times` function. The function works by iterating over each substring of the passed string, with a length equal to the passed substring and counting the number of times the substring appears. It also accounts for the case where the passed string and substring are the same, so it only counts one instance. 
The if `__name__ == "__main__":` line ensures that the test case is run when the script is executed directly.  It can be executed directly by running `python script_name.py`