```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Unit tests
string1 = 'xyzXYZ'
assertEqual(count_distinct_characters(string1), 3)

string2 = 'jerry'
assertEqual(count_distinct_characters(string2), 4)

string3 = '!JERRY.'
assertEqual(count_distinct_characters(string3), 3)

string4 = 'ABCDEFGHIJKLMNOPQRSTUVabcdef'
assertEqual(count_distinct_characters(string4), 8)
```
The function `count_distinct_characters` calculates the number of distinct characters in a given string, regardless of case. It uses `set` to convert all characters to lowercase and then counts the distinct ones. The test cases cover various strings and ensure that the function works correctly.