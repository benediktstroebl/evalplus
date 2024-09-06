Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The count_distinct_characters function takes a string as input and returns the number of distinct characters in the string, regardless of case. In the code, the function creates a characters set to hold the distinct characters in the string by converting the input string to lowercase using the lower() method. This ensures that 'x', 'X', and 'xX' are considered the same character. Finally, it returns the length of the characters set, which is the number of distinct characters in the string. 

Here's an example usage in the solution's corresponding test to verify the function's behavior:
```python
# Test the function through its behavior on predefined samples 
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
```