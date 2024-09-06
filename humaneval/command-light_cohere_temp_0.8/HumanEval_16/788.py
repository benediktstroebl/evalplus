```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Basic tests
string = 'xyzXYZ'
assert count_distinct_characters(string) == 3

string = 'jerry'
assert count_distinct_characters(string) == 4

# Longer string
string = 'a'b'c'deface'b' Rost'bb'cc''b'a'X'z'''
assert count_distinct_characters(string) == 10

# Invalid input
try:
    count_distinct_characters('')
except AssertionError as e:
    print(f'Error: {str(e)}')
```