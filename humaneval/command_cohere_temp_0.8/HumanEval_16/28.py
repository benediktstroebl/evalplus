Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This code defines a function, `count_distinct_characters`, which takes a string as an argument and uses a set data structure to store the unique characters in the string regardless of case. The `lower()` method is used to convert the characters in the string to lowercase before they are inserted into the set. Finally, the length of the set is returned, which represents the number of distinct characters in the string.  This approach ensures that only distinct characters are counted, and the case is ignored for character uniqueness.