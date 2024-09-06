Here's a self-contained Python function that finds the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, considering overlapping cases.
    >>> string = "aaaaaaa"
    sub = "aa"
    ret = 0
    for i in range(len(string)):
        if string[i] == sub:
            ret += 1
    return ret
    """

# Test case 1
test_1 = how_many_times('aaaaaaa', 'aa')
assert test_1 == 3

# Test case 2
test_2 = how_many_times('hello world', 'l')
assert test_2 == 4
```
This function will return the number of occurrences of the substring in the string, considering cases where the substring is present multiple times.