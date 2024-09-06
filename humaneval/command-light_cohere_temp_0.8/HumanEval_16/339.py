```python
def count_distinct_characters(string):
    """
    counts the number of distinct characters in the given string, regardless of case
    """
    char_counts = {}
    for char in string.lower():
       
       
        char_counts[char] = char_counts.setdefault(char, 1)
    return len(char_counts)

#tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3

def test_count_distinct_characters2():
    assert count_distinct_characters('Jerry') == 4
```