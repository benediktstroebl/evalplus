```python
def count_distinct_characters(string: str):
    return len(set(string))

# Tests go here
'a'
count_distinct_characters('abc') should return 2
'b'
count_distinct_characters('xyzXYZ') should return 3
'c'
count_distinct_characters('ABC') should return 2
'd'
count_distinct_characters('') should return 0
```