Here is a Python script that contains a self-contained function to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 unique characters in the string
```
This function uses a set of characters in the input string and iterates over each character. It then checks if each character is in the set, and counts the number of distinct characters. The function then returns the distinct characters count.