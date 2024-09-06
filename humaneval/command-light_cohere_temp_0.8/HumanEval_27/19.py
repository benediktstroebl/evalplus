```python
def flip_case(string: str) -> str:
    return ''.join capitalization(string)

def test_flip_case() -> None:
    assert flip_case('hello') == 'H EllO'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('hello world!>'') == 'hello W olld'
    assert flip_case('hello@world') == 'hello@wORLD'
```
The function `flip_case` takes a string as input and returns a string with characters flipped between lowercase and uppercase. The `test_flip_case` function contains tests that verify the correctness of the `flip_case` function.