Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the code and some example tests:
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
assert how_many_times('aaabbb', 'ab') == 2
```

The function `how_many_times` takes two strings as input: `string` and `substring`. It counts how many times the `substring` can be found in the `string`, including overlapping instances. The function uses a loop to compare consecutive substring lengths of the input `string` with the desired `substring`. The count is incremented each time a match is found.

The test cases cover various scenarios to validate the function's behavior and ensure it provides the correct count for different cases of substrings within the main string.