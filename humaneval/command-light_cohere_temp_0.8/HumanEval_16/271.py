```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string() if c.isalpha()})
 unique character
    return

# Unit tests
test_count_distinct_characters("hello world")
    assert count_distinct_characters("hello world") == 5

test_count_distinct_characters("xVaLL")
    assert count_distinct_characters("xVaLL") == 4

test_count_distinct_characters("JER")
    assert count_distinct_characters("JER") == 4

test_count_distinct_characters("XYZ")
    assert count_distinct_characters("XYZ") == 3

test_count_distinct_characters("jerry")
    assert count_distinct_characters("jerry") == 5

test_count_distinct_characters("hello ")
    assert count_distinct_characters("hello ") == 26

test_count_distinct_characters("-A")
    assert count_distinct_characters("-A") == 26
```