```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abcABC') == 3
assert count_distinct_characters('jerry') == 4

# Main code
if __name__ == "__main__":
    test_count_distinct_characters()
 ```
The solution uses the built-in Python function `len(set(string))` to count the number of unique characters in a given string. It utilizes `set()` and `str` to convert the string into a set of characters, and then uses the `len()` function to count the elements in the set. The output is the number of distinct characters.