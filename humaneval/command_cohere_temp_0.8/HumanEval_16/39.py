Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This code defines a function, `count_distinct_characters`, which takes a string as an argument and calculates the number of distinct characters within the string, regardless of case. It does this by converting the input string to lowercase and then using a `set` to automatically filter out duplicate characters.  The `set` data structure only allows unique values, so directly converting the string to a set would give the desired result. Finally, it returns the count of distinct characters. The function is tested with the provided example cases and passes. 

Here's the entire code for clarity:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)

# Test Cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
```