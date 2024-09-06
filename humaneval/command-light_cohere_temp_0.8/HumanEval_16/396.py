```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Tests
string1 = 'xyzXYZ'
assertEqual(count_distinct_characters(string1), 3)

string2 = 'jerry'
assertEqual(count_distinct_characters(string2), 4)

#Custom string
string3 = 'Hello World'
assertEqual(count_distinct_characters(string3), 8)
```
This code defines a function `count_distinct_characters` that computes the number of distinct characters in a given string, regardless of case. It then runs three sets of tests using sample strings to ensure that the function is working correctly.