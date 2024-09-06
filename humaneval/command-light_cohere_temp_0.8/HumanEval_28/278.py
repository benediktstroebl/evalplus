```python
def concatenate(strings: List[str]) -> str:
    return "".join(strings)

# Test case: empty list
test_empty()
def test_empty():
    assert concatenate([]) == ""

# Test case: basic strings
test_basic()
def test_basic():
    assert concatenate(['a', 'b', 'c']) == 'abc'

if __name__ == "__main__":
    test_empty()
    test_basic()
```

The function `concatenate` takes a list of strings as input and returns a single string by concatenating the strings in the list. The `test_basic` function verifies that this function works correctly by testing with basic strings. The script is designed to be self-contained, meaning it can be run without further imports or external functions.