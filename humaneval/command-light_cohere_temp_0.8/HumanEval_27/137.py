```python
def flip_case(string: str) -> str:
    return ''.join(''.join(c.swap(). using_case(c) for c in string)

# Example function test
def test(f: FlipCase) -> None:
    assert f('Hello') == 'Helles'
    assert f('world') == 'dlrowO'
    assert f('FOO') == 'ooF'
    assert f('123') == '231'
    assert f('abc') == 'Cba'
    assert f('@#$%^&*()') == '@#$%^&*u'
    return

# Call the function with test to run the test suite.
test(flip_case)
```