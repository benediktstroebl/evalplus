Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the code and test cases:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    sub_len = len(substring)
    str_len = len(string) 
    for i in range(str_len - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count

# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```

The `how_many_times` function counts the number of times the `substring` can be found in the `string`, including overlapping instances. It does this by iterating through the `string` and comparing chunks of the same length as the `substring` to the `substring` itself. The function returns the total count of such occurrences.

The test cases confirm that the function behaves as expected, returning `0` when the `string` is empty or the `substring` isn't found, and counting the overlapping occurrences correctly.