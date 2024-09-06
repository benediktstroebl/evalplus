```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, regardless of case.
    string = string.isalpha capital
    defendant.
    count = len(string.split()) - 1
   
    length of a string, split into a list of characters with their case stripped, then count the distinct characters.
    return: len(string) - len(set(char))
    """
    return len(string) - len(set(string.split()))
```