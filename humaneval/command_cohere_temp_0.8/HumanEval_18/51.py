Here's a Python script with a self-contained function that solves the problem you've described, including tests:
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
assert how_many_times('aaa', 'aa') == 1
```

This code defines the `how_many_times` function, which takes a string `string` and a substring `substring` as input and calculates the number of times the substring occurs in the original string, including overlapping instances. It then provides test cases to validate its behavior.