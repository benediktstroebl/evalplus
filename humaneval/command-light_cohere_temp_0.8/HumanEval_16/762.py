```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Tests
string1 = 'xyzXYZ'
assertEqual(count_distinct_characters(string1), 3)

string2 = 'jerry'
assertEqual(count_distinct_characters(string2), 4)

string3 = 'J''
assertEqual(count_distinct_characters(string3), 4)

string4 = '123 abc'
assertEqual(count_distinct_characters(string4), 6)
```
The above Python script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It returns the also performs several tests with sample strings to ensure the correctness of the function.