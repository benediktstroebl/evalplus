```python
def count_distinct_characters(string):
    return len({c for c in string.fill(str.lower()) for c in string if c != ' '})

#Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('Jerry'), 4)
assertEqual(count_distinct_characters(' ''), 3)
assertEqual(count_distinct_characters(' 'abc'), 3)
assertEqual(count_distinct_characters('ABC'), 3)
assertEqual(count_distinct_characters('123'), 3)
assertEqual(count_distinct_characters('\u4F00'), 4)
```