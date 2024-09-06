Here's a Python script with a self-contained function that solves the problem you've outlined, including a markdown code block and a corresponding test case:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    substring_length = len(substring)
    string_length = len(string) 
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count

# Test case
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('', 'a') == 0
```
This script defines the `how_many_times` function, which takes a string `string` and a substring `substring` as input and returns the number of times the substring occurs within the string, including overlapping occurrences. It uses a for loop to iterate over the string and checks each substring of length equal to the length of the substring, and counts the number of matches.

The function is tested with three cases: empty input, a single-letter substring, and a two-letter substring. It is designed to handle these cases and provide the correct answer for each scenario. 
The description of the function and the test cases are included to make the code more understandable and self-contained.