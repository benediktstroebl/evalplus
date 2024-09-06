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
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script defines a function `how_many_times` that takes a string `string` and a substring `substring` as input, and counts the number of times the substring occurs in the string, including overlapping instances. The function uses a loop to compare the substring to consecutive portions of the original string, and increments the count if there's a match. The script also includes test cases to demonstrate the function's behavior.