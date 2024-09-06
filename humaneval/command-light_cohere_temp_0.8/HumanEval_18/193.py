```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i] == substring:
            count += 1
    return count

# Test the function
# Input string is a simple capital letter
input_string = "A"
# Test string length
assert len(how_many_times(input_string, "A")) == 5

# Test substring
input_substring = "aa"
# Test input string length
assert len(input_string) == 3
assert len(how_many_times(input_string, input_substring)) == 3

# Test both characters
input_substring = "aaa"
input_string = "aaaa"
# Test if substring length > input string length
assert len(input_string) == 3
assert len(how_many_times(input_string, input_substring)) == 2

# Test for overlapping substring
input_substring = "aa"
input_string = "aaaa"
assert len(input_string) == 3
assert len(how_many_times(input_string, input_substring)) == 3

```
This script defines a function `how_many_times` that takes two parameters: a string and a substring. The function then returns the how many times the substring can be found in the original string. It uses a basic approach by using a counter and iterating over the input string.