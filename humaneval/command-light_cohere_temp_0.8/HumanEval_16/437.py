Here is a self-contained Python script with a function that solves the problem of counting distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isalpha()}
    particular

def test_distinct_characters(test_string: str) -> None:
    assert count_distinct_characters(test_string) == len(test_string)
    return
test_distinct_characters('xyzXYZ')
test_distinct_characters('Jerry')
```
The `count_distinct_characters` function calculates the number of distinct characters in the input string by using a generator expression and the `len` function. The `test_distinct_characters` function acts as a testing suite for the `count_distinct_characters` function, passing various test strings and verifying the output of the `count_distinct_characters` function matches the length of the test string.