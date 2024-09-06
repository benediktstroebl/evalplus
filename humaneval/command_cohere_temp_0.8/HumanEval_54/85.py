```python
def same_chars(s0, s1):
    return sorted(s0) == sorted(s1)
```

The idea is to sort the characters in the strings and then compare them. If the characters are the same, the sorted results will also be the same:
```python
def test_same_chars():
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert same_chars('abcd', 'dddddddabc') == True
    assert same_chars('dddddddabc', 'abcd') == True
    assert same_chars('eabcd', 'dddddddabc') == False
    assert same_chars('abcd', 'dddddddabce') == False
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False
```