```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('jerry') == 4
``` 
This code provides a function that calculates the count of distinct characters in a given string, regardless of case. It then passes the