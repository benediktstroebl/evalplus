```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function with a string that has duplicate characters
test_count_distinct_characters = "JERRY"
assert count_distinct_characters(test_count_distinct_characters) == 4

# Test the function with a string that has no duplicates
test_single_character = "a"
assert count_distinct_characters(test_single_character) == 1
```
This Python code defines a function called **count_distinct_characters** that takes a string as input and returns the number of unique characters in that string, regardless of case. This is using the's set of characters in the string and counting the number of distinct elements.