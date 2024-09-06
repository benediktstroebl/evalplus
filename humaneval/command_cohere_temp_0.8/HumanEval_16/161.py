Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The `count_distinct_characters` function takes a string as an argument and returns the number of distinct characters (regardless of case) in the string. It uses a set to store the characters, ensuring that each character is unique, and then counts the number of distinct characters in the set. The `lower()` method is used to convert the characters in the string to lowercase before inserting them into the set, ensuring that case-insensitivity. 

Here's an example usage:
```python
print(count_distinct_characters('xyzXYZ'))  # Outputs: 3
print(count_distinct_characters('Jerry'))  # Outputs: 4
```
This method ensures a quick and reliable calculation of the number of distinct characters.