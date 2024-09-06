```python
def count_distinct_characters(string):
    return len({c for c in string.string().a if c.isalpha()}

```

# Test case using a markdown code block
tests = {
    """ Test string for character count distinctness
    "+xyzXYZ+"
    """
    assert count_distinct_characters('+xyzXYZ+') == 3
    """ Test string for lowercase characters only
    "jerry"
    """
    assert count_distinct_characters('jerry') == 4
}
```