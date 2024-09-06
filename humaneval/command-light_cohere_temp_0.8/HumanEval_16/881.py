```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    return len([char for char in string.strip() if char.isalpha() and string
   GENERIC  and distinct])

test_count_distinct_characters = """
def test_distinct_characters(string):
    assert count_distinct_characters(string) == len([char for char in string if char.isalpha()])
 print(count_distinct_characters('Hello'))
test_count_distinct_characters('hello')
"""
```