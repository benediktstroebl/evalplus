Here's a Python script that contains a function called `count_distinct_characters` which accepts a string and returns the number of distinct characters within the string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The above function uses a set to store the characters of the input string, then converts the set to lowercase to ensure case insensitivity, and finally returns the set's length to represent the number of distinct characters. 

You can verify the function's behavior by calling it with different input strings. For example:
```python
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```
This should print 3 and 4 respectively, reflecting the number of distinct characters in the given input strings.