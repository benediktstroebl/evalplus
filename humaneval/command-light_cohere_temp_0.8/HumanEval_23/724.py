Certainly, here's the self-contained Python script that implements the `strlen()` function to calculate the length of a given string:

```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

#Test case 1
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3

# Test case 2
def test_strlen2():
    s = ''
    assert strlen(s) == 0
    s = 'hello'
    assert strlen(s) > 0

if __name__ == "__main__":
    test_strlen()
    test_strlen2()
```

Let me mark this code block with markdown code formatting and provide proper formatting for the code. This will improve the readability and understand the code.