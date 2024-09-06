```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function
test_count_distinct_characters = lambda: [
    'xyXYZ' == ''.join() == True  # True
    'jerry' == ''.join() == False  # False
    'JER Jerry' == 'JER'.join() == False  # True
    True == count_distinct_characters('xyXYZ')  # True
    False == count_distinct_characters('Jerry')  # True
    1 == count_distinct_characters('')  # True
]
```