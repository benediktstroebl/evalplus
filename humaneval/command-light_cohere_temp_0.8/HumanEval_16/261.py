```python
def count_distinct_characters(string: str) -> int:
    characters = set(string)
    return len(characters)

# Test the function with different inputs
# Test with empty string
test_empty() => 2
# Test with only spaces
test_spaces() => 4
# Test with all ASCII uppercase and lowercase English letters (including spaces)
test_all_chars() => 13
# Test with only numbers
test_numbers() => 10
# Test with a mix of characters
test_mixed() => 9
``` 
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. The set of characters in the input string is used to create a set, and the length of this set is returned as the number of distinct characters. This code can be easily tested using various inputs, including empty strings, spaces, all ASCII uppercase and lowercase English letters, and numbers, and the results can be compared to ensure that the function is correct.