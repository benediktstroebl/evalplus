```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 distinct
```
The function counts the number of distinct characters in the string, regardless of case. It uses a set of characters and a list comprehension with the str.s unique function to filter out all characters from the string and count the number of distinct characters.