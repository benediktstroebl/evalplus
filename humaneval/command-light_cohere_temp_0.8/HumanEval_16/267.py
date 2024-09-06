```python
def count_distinct_characters(string):
    return len([c for c in string.md_lower() if c not in string])

# Tests
string1 = 'xyzXYZ'
assert count_distinct_characters(string1) == 3

string2 = 'jerry'
assert count_distinct_characters(string2) == 4

string3 = 'abc123xyz'
assert count_distinct_characters(string3) == 6

```
The function count_distinct_characters takes a string as input and returns the number of distinct characters in that string, regardless of case. The function uses a lower() method to convert each character in the string to lowercase and then iterates through the resulting list, adding a character to the distinct list if it is not already present in the string. The function then returns the string.