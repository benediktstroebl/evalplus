```python
def count_distinct_characters(string):
    return len({c for c in string. characters() if c not in 'abcdefghijklmnopqr'})

# Test cases
string1 = 'xyzXYZ'
assert count_distinct_characters(string1) == 3

string2 = 'jerry'
assert count_distinct_characters(string2) == 4

string3 = 'hello world'
assert count_distinct_characters(string3) == 13 

```