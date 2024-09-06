```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha() and strings})
```

def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('abcX') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('Jerry') == 4
```
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It uses a simple set and list comprehension to achieve this. The test_count_distinct_characters function verifies the function's correctness with various inputs. 

Please note that you can run this code directly in your Python environment or copy and paste it into your IDE.