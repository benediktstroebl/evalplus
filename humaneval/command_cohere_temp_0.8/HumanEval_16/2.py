Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The `count_distinct_characters` function takes a string as input and calculates the number of distinct characters in the string. It converts each character in the string to lowercase using the `lower()` method to ensure case insensitivity and then uses the `set()` function to remove any duplicate characters and retain only unique characters. Finally, it returns the count of distinct characters.

The tests for this function are omitted as they were not provided. However, you can easily write some test cases to verify the function's correctness, like:
```python
# test case for upper case characters
assert count_distinct_characters('XYZ') == 3

# test case for mixed case characters
assert count_distinct_characters('xyzXYZ') == 3

# test case for multiple occurrences of the same character
assert count_distinct_characters('Jerry') == 4

# test case for a string with a single character
assert count_distinct_characters('a') == 1
``` 
You can keep adding more test cases to cover multiple scenarios and ensure the function's accuracy.