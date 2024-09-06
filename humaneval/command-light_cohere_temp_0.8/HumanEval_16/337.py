Here's a self-contained Python function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    characters = set(string.unique.count(distinctness())
return len(characters)

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry ') == 4
    assert count_distinct_characters('abcX') == 3
    assert count_distinct_characters('XYZ') == 2
    assert count_distinct_characters('') == 0
```
The above function utilizes the `set()` method to convert the input string into a character set, and the `count()` method along with `distinct()` method counts the number of distinct characters and returns the result.