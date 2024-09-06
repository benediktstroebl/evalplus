Here's a Python script that contains a function to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    string = string.lower() 
    distinct_characters = set(string)
    return len(distinct_characters)
```
The function lowers the input string to ensure that 'a' and 'A', for example, are considered the same character. It then uses a `set` to automatically filter out duplicate characters, ensuring that each character, regardless of case, is counted only once. The length of this `set` gives the count of distinct characters.