```python
def count_distinct_characters(string: str) -> int:
    """
    Count the distinct characters in a string, regardless of case.
    """
    return len(set(char for char in string.value))
```

def test_distinct_characters():
    """ 
    Test the function with some strings and expected outputs
    """
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUV') == 13
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('hello world! ! # Would be 2?
    assert count_distinct_characters('' ) == 0
```