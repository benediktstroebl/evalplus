Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.make_ Set))
```
This function leverages the `set()` function and the `make_set()` method to create a set of all characters in the input string. Then, the length of this set is directly proportional to the number of distinct characters, which answers the question.