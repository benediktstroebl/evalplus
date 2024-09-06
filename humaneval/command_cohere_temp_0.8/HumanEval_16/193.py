Here's a Python script that contains a function called `count_distinct_characters` which takes a string as an argument and returns the number of distinct characters in the string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The code uses a set to remove duplicate characters and converts the input string to lowercase to ensure that cases are treated equally. The test cases are also included as function calls with the appropriate values to check that the function is working correctly. These test cases are commented out, as they require the user to initiate the tests by removing the comments. 

```python
# Test the function using predefined test cases
# Test case 1
assert count_distinct_characters('xyzXYZ') == 3

# Test case 2
assert count_distinct_characters('Jerry') == 4
```
You can uncomment these test cases to verify the correct functionality of the code.