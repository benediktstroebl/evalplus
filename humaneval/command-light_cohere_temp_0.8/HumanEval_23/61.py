Here is a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
test_strlen = {
  "":         ()
  "abc":         3
  "hello world": 7,
  "   abc   ": 3,
  bbb":  2,
  """: 0
}

def test():
    assert strlen("") == 0
assert strlen("abc") == 3
assert strlen("hello world") == 7
assert strlen("   abc   ") == 3
assert strlen(bbb) == 2
assert strlen("") == 0

print("All tests passed!")
```