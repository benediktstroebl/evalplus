```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

# Test case 1
assertEqual(count_distinct_characters('xyzXYZ'), 3)

# Test case 2
assertEqual(count_distinct_characters('jerry'), 4)

# Test case 3
string = 'a' + 'bc' + 'a' + 'xx' + ' Baz' + 'xx' + 'a' + 'bb'
assertEqual(count_distinct_characters(string), 7)

# Test case 4
string = 'this is a 'long' ' string to test distinct character counting
assertEqual(count_distinct_characters(string), 25)
```