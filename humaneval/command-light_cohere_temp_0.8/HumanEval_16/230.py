```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This script defines a function that takes a string as input and returns the count of distinct characters in that string, regardless of their case. The function uses the string.lower() method to convert all input string to lowercase, then uses the len(set()) function along with the set() constructor to create a set of all the characters in the string. Finally, it uses the len() function to get the number of elements in the set, which is the count of distinct characters in the string.