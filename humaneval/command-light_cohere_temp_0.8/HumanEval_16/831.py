```python
def count_distinct_characters(string: str):
    return len(set(string.isalpha()))
```

This Python function counts the number of distinct characters in a given string, regardless of case. The function uses the set() to convert all characters in the string to lowercase and then uses the len() function to count the number of unique characters.

The time complexity of this solution is O(n), where n is the length of the input string, as it involves creating a set of characters and performing a length check.

The space complexity is O(1), as it only uses a constant amount of extra space regardless of the input size.