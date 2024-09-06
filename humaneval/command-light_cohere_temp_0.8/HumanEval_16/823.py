```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})
 how many distinct characters does it consist of?

def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters(' ABC') == 3
    assert count_distinct_characters(' aBC') == 3
    assert count_distinct_characters('XyXyX') == 3
    assert count_distinct_characters(' jerry ') == 4


if __name__ == "__main__":
    test_distinct_characters()
```  The above code defines a function count_distinct_characters that returns the count of distinct characters in a given string. It also has a test_distinct_characters function that does the same but returns boolean values (True or False) instead of integers, to test the correctness of the count_distinct_characters function.