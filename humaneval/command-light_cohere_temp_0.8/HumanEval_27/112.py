```python
def flip_case(string: str) -> str:
    """
    Converts all character case from lowercase to uppercase and vice versa.
    Returns theoo original case string.
    """
```
def test_flip_case()():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'oooRD'
    assert flip_case('RAM') == 'amRa'
    assert flip_case('!!#! ') != '##'
    assert flip_case('   ) == '!!'
```