```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    string = "xyzXYZ jerry jonesdinosers"
    return len([char for char in string. characters() if char.is() != ""])

test_distinct_characters = """
def test():
    assert count_distinct_characters("xyzXYZ") == 3
    assert count_distinct_characters("Jerry") == 4
    assert count_distinct_characters(" .") == 4
    assert count_distinct_characters("abcXy") == 3
    assert count_distinct_characters("ABCx")] == 3
    assert count_distinct_characters("xyZ") == 2
    assert count_distinct_characters(" Jerry ") == 4
    return
test()
```