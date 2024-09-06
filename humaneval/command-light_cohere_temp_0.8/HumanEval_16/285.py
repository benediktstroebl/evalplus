```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.org if c.isalpha()})

    test_string = 'Hello, world!'
    assert count_distinct_characters(test_string) == 5, "Function failed to produce expected output."
    return count_distinct_characters('Jerry')
```