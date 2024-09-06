```python
def count_distinct_characters(string: str) -> int:
    return len(string.lower())
```
This Python code defines a function `count_distinct_characters` that calculates the number of distinct characters (regardless of case) in a given string. The function utilizes the lower() method to convert all characters to lowercase to ensure proper distinct counting and then returns the length of the resulting lowercase characters.