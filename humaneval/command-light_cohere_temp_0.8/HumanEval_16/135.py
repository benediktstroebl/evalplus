Here is a Python script that contains a self-contained function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This script defines a function that counts the number of distinct characters in a string, regardless of case. The function uses the set and the lower() method to convert all characters to lowercase, then uses the len() function to count the number of unique characters.