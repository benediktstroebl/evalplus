```python
def count_distinct_characters(string):
    """ Returns the number of distinct characters in the string (case-insensitive)"""
    return len([c for c in string.isalpha()])

# Test
def test_function():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry ') == 4
    assert count_distinct_characters('ABC') == 3
    assert count_distinct_characters('Abc') == 3
    assert count_distinct_characters('abCD') == 3
    assert count_distinct_characters('  https://cohere.ai ') == 4  # Invalid input: This is an example of a bad string that will cause an error.
 I hope this explanation helps you better understand how the code works.