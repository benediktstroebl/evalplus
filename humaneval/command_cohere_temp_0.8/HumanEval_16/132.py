Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
This script defines a function `count_distinct_characters` which takes a string as an argument and returns an integer indicating the number of distinct characters in the string, regardless of case. 

The function uses a set to store the characters, removing any duplicate characters and converting all characters to lowercase, to ensure that characters like 'X' and 'x' are counted as the same character. 

This approach provides a straightforward solution to the problem in a self-contained manner, as it doesn't rely on any external libraries or modules. 

To verify the correctness of the function, you can run tests like this:
```python
# Test case one
print(count_distinct_characters('xyzXYZ')) # Output: 3

# Test case two
print(count_distinct_characters('Jerry'))  # Output: 4
```
This demonstrates how the function can be used and the expected output is provided directly in the script, following the spirit of unittest frameworks. 

Let me know if you would like to have the tests structured in a more formalized manner using an actual unittest framework or if you'd like to proceed with another problem.