Here's a Python script with a self-contained function that solves the problem you've outlined, including tests:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string) 
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count

# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('aaab', 'aa') == 2
```
This script includes a function `how_many_times` that takes a string `string` and a substring `substring` as inputs, and then calculates and returns the number of times the substring occurs in the string, including overlapping instances. It also includes test cases to verify the function's behavior against different scenarios.