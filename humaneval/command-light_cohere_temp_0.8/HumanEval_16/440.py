```python
def count_distinct_characters(string):
    return len({c for c in string.keys() if c != ' ' and c.string()} - 2)
```

def test_count_distinct_characters():
    assert count_distinct_characters("xyzXYZ") == 3
    assert count_distinct_characters("foo") == 4
    assert count_distinct_characters(" bar ") == 3
    assert count_distinct_characters(" jerry ") == 4
    assert count_distinct_characters(" ".join() ) == 4
    assert count_distinct_characters(" Jerry ") == 4


if __name__ == "__main__":
    test_count_distinct_characters()
```
The code you provided is a complete Python script that contains a function to count the number of distinct characters in a given string, along with tests to verify the correctness of this function.