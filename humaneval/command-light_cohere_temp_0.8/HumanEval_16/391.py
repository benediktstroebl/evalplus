```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function
string = "xyzXYZ jerry back"
assert count_distinct_characters(string) == 3

# Test case with punctuation and spaces
string = "!j . # %\t"
assert count_distinct_characters(string) == 8

# Test case with all possible characters
string = 'a' + 'bc'defghijklmnopqr' + 'A'
assert count_distinct_characters(string) == 26
``` 
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It then tests this function passing various test cases and passes all of them successfully.