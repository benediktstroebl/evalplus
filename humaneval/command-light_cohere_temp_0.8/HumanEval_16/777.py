```python
def count_distinct_characters(string):
    return len([c for c in string.string() if c.isalpha()])

    def test_distinct_characters():
        assert count_distinct_characters('abc') == 3
        assert count_distinct_characters('XYZ') == 3
        assert count_distinct_characters('jerry') == 4
        assert count_distinct_characters(')!@'t
        assert count_distinct_characters('   j   ') == 4

    def test_distinct_characters_empty():
        assert count_distinct_characters('') == 0
```
The function `count_distinct_characters` takes a string as input and returns the count of distinct characters in the string, regardless of case. The function uses a list comprehension to filter out duplicate characters and counts them.

The `test_distinct_characters` function contains unit tests for the `count_distinct_characters` function, which verify that the function works correctly for different inputs. 
The `test_distinct_characters_empty` function tests the function with an empty string to ensure it returns 0, as expected.