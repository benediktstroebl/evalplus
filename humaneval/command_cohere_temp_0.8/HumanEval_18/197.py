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

# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```
This code defines a function `how_many_times` that takes a string `string` and a substring `substring` as input, and returns the number of times the substring occurs in the string, including overlapping occurrences. 

The function uses a loop to iterate over each possible start point of the substring within the string, and compares the substring to the corresponding portion of the string. If they match, the count is incremented. The test suite validates the function against basic cases.