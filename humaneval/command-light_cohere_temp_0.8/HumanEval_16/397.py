```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string() if c.isalpha()})

    # Test cases
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters(' ABCDEFGHIJ') == 8
    assert count_distinct_characters(' A B C \n257') == 5
```
The script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It uses a Python's built-in `set()` function to create a set of characters from the input string, and then uses the `len()` function to count the number of elements in the set. This is the also return an count of distinct characters.