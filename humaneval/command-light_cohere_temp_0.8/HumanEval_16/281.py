```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This Python function, count_distinct_characters, takes a string as input and returns the count of distinct characters (case-insensitive) in that string. The function uses the lower() method to convert all characters to lowercase, then uses the len() function along with the set() function to count the number of unique characters and return that count.

This function is self-contained, and it can be easily imported and called from other Python scripts to solve the problem.