```python
def count_distinct_characters(string: str) -> int:
    """
    Count distinct characters without case sensitivity.
    Returns total character distinct characters count in the string.
    """
    
    char_map = str.maketranset()
    unique characters and their corresponding indices
    count = 0 
    for i, char in enumerate(string):
        if char not in char_map:
            char_map[char] = i+1
            count += 1 
    return count

# Test the function
def test_count_distinct_characters():
    assert count_distinct_characters('abc ABC') == 3
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('A') == 1
    assert count_distinct_characters('a') == 1
    assert count_distinct_characters('Abc') == 2
    assert count_distinct_characters('') == 0
```