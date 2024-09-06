```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha() and
        same letter or certain letter is unique (case-insensitive))
    return len(string) - len(set(string))

# Unit tests
string1 = "xyzXYZ"
assertEqual(count_distinct_characters(string1), 3)

string2 = "jerry"
assertEqual(count_distinct_characters(string2), 4)

# Run the code and compare the test results
```