```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.count(c for c in string if c.isalpha()))
``` 
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry ') == 4
```  This code defines a function **count_distinct_characters** that calculates the count of distinct characters in a given string, regardless of case. It then tests this function with test cases to ensure the correctness of the code.