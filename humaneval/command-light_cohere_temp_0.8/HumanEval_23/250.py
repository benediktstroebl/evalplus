```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Tests
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen(' dear') > 3  # True

# Usage
if __name__ == "__main__":
    print(test_strlen())
```