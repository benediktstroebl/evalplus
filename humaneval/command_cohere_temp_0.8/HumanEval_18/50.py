Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
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
This script defines the `how_many_times` function, which takes a string `string` and a substring `substring` as input and returns the number of times the `substring` occurs in the `string`, including overlapping occurrences. 

The function uses a loop to iterate over each possible start point of the substring within the string, and checks if the substrings match. The number of matches is counted and returned.

The test cases confirm that the function works correctly for the example use cases provided in the original description. You can add more tests to cover other scenarios and ensure the function's correctness.  The code is enclosed in a code block and is formatted for readability.