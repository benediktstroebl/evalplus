```python
def strlen(string: str) -> int:
    return len(string)

#Test string length function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('123') == 3
    assert strlen('abcabc') == 6
    assert strlen('') == 0
```