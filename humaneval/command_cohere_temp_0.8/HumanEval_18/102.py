Here's a Python script with a self-contained function that solves the problem you've outlined, including markdown code blocks with example inputs and expected outputs:
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
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```
This script includes a function `how_many_times` that takes a string `string` and a substring `substring` as inputs, and returns the number of times the substring occurs in the string, including overlapping instances. The function uses a loop to iterate over possible starts for the substring and compares it to the full string to identify the occurrences.

The code includes example inputs and expected outputs in the form of assert statements. These checks ensure that the function behaves as expected and aligns with the problem definition. In particular, it checks for an empty string, a string with one repetition of the substring, and a string with multiple overlapping occurrences of the substring. 

Note that this code assumes the existence of a `assert` statement, which is a standard Python feature used for testing and validating assumptions. If you're running this code in a context where `assert` is not recognized, you might need to define it explicitly.