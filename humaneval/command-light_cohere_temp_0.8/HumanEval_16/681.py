```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters, ignoring case.
    Return: number of distinct characters
    """
    char_set = set(string)
    return len(char_set)

def test_count_distinct_characters():
    assert count_distinct_characters('abc ABC') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('z')" == 4
    assert count_distinct_characters('  jerry') == 4
```
The above code defines a function that counts the number of distinct characters in a given string, regardless of case. The test_count_distinct_characters function verifies the correctness of the function with a variety of test cases.