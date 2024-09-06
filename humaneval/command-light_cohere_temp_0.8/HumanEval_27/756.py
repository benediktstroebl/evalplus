```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else(c.islower()) else(c) else c.isupper())

    # tests
    assert flip_case('hello') == 'HElLO'
    assert flip_case('HEllO') == 'hello'
    assert flip_case('world') == 'dwORld'
    assert flip_case(' Theod'] == 'doTeD'
    return flip_case('')
```