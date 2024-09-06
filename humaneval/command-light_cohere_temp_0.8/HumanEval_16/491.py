```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.isupper()))
```
This script defines a function, count_distinct_characters, which takes a string as input and returns the count of distinct characters (regardless of case). It uses the set() of characters in the string and the isupper() method to convert all characters to uppercase before performing the set operation, which automatically removes duplicates and counts distinct characters. 

This function is self-contained and efficiently solves the problem of counting distinct characters in a given string.