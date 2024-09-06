Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the code and some example tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    idx = 0
    while idx < len(string):
        idx2 = string.find(substring, idx)
        if idx2 == -1:
            break
        count += 1
        idx = idx2 + 1
    return count

# Tests
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```

The `how_many_times` function iterates through the larger string, using the `find` function to search for the substring. The `find` function returns the first index of the substring, or -1 if it's not found. The function then increments the count if the substring is found, and continues searching from the next index by adding 1 to the index of the substring. The function returns the final count of occurrences of the substring. 

The tests assert the function's correctness in handling different cases.