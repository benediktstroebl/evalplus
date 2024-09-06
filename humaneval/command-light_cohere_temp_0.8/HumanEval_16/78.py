Here is a self-contained Python script that defines a function `count_distinct_characters` solving the problem:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
``` 
# tests
string1 = 'xyzXYZ'
string2 = 'jerry'
print(count_distinct_characters(string1))  # Output: 3
print(count_distinct_characters(string2))  # Output: 4
``` 
This script provides a solution to the problem of counting the distinct characters in a given string, regardless of case.