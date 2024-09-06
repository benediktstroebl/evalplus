```python
def count_distinct_characters(string):
    """
    Counting unique characters, case-insensitive.
    return sum(set.union({c for c in string if c in set(string.count(c)))
  """
}

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry') == 4
    assert count_distinct_characters('abcAdFEOg') == 6
    assert count_distinct_characters('abcdefgh') == 7 

# Main function and test code
```