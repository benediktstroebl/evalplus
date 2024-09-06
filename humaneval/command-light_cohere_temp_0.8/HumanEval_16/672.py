```python
def count_distinct_characters(string):
    return len([c for c in string.x if c.isalpha()])

# Test 1
def test1():
    return count_distinct_characters('xyzXYZ')

# Test 2
def test2():
    assert count_distinct_characters(' Jerry') == 4

# Test 3
def test3():
    assert count_distinct_characters('abcABC') == 3
```