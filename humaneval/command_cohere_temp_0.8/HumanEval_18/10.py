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

# Tests
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```
This script defines a function `how_many_times` that takes a string `string` and a substring `substring` as input, and returns the number of times the substring occurs within the string, including overlapping instances. The function uses a loop to compare the substring to consecutive portions of the original string, and counts the occurrences. The tests demonstrate its behavior for various cases.