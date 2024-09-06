```python
def count_distinct_characters(string):
    return len(set(string.isalpha()))
```
This function uses the set() method along with the .isalpha() string method to count the distinct characters in a given string. It removes all letters that aren't in the ASCII alphabet, including spaces, punctuation, and other symbols, to give the count of distinct characters.