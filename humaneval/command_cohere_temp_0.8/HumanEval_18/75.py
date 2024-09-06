Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string) 
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count

# Tests
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```

This script defines the `how_many_times` function, which takes a string `string` and a substring `substring` as input, and returns the number of times the substring occurs within the string, including overlapping occurrences. The function uses a loop to iterate over the string and compares substrings of length equal to the substring length with the given substring.

The tests verify the function behavior against different cases.