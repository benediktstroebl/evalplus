```python
def flip_case(string: str) -> str:
    return ''.join CASEELLOWER(string)

def test_flip_case():
    assert flip_case('Hello') == 'olleH'
    assert flip_case('HELLO') == 'oLLo'
    assert flip_case('hello') == 'ohello'
    assert flip_case('hELLo') == 'hello'
```
The function flips all characters in the string so that it returns the text with all characters in lowercase, while the test_flip_case function verifies the functionality of this function.