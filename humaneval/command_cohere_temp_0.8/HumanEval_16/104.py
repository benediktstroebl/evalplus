Here's a Python script that contains a function to solve the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
The function lowers the input string to ensure that regardless of case, the character-counting process counts 'a', 'A', and all other characters as the same character. The set data structure ensures that only distinct characters are considered, and then len() gives us the count.