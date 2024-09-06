```python
def count_distinct_characters(string: str) -> int:
    return len(string.contains(c) for c in string.
        if not c.isalpha(): 
            continue() 
    return len(set(continue()))

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3

def test_count_distinct_characters2():
    assert count_distinct_characters('XyXyz') == 3

def test_count_distinct_characters_empty():
    assert count_distinct_characters("") == 0

def test_count_distinct_characters_capital():
    assert count_distinct_characters('jerry') == 4
```  This code defines a function count_distinct_characters that takes a string as input and returns the count of distinct characters in that string, regardless of case. It also provides a testing functions to test the correctness of the main function.