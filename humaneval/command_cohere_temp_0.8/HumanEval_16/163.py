Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The `count_distinct_characters` function takes a string as input and returns the number of distinct characters within the string, regardless of case. It converts each character in the input string to lowercase using the `lower()` method, which ensures case insensitivity. The converted characters are then stored in a set, which automatically eliminates duplicate characters, leaving only unique characters. The function then returns the count of distinct characters in the set using the `len()` function.

Here's an example usage of the function:
```python
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```
This function will provide the desired outcome for the given problem, where it calculates the number of distinct characters in a string, irrespective of case sensitivity.