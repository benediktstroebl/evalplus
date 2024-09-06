Here's a Python script that contains a function called `count_distinct_characters` which accepts a string `s` as argument and returns the number of distinct characters in the string, regardless of case:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to eliminate duplicate characters and then converts the string to lowercase to ensure that cases are not considered when counting. The test cases provided in the original problem should evaluate to 3 and 4, respectively.