Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The `count_distinct_characters` function takes a string as input and returns the number of distinct characters in the string, regardless of case. It converts the input string to lowercase to ensure that uppercase and lowercase variations of each character are considered identical. Then it uses a `set` to keep only unique characters, benefiting from the intrinsic uniqueness of a set.  Finally, it returns the count of distinct characters in the string.