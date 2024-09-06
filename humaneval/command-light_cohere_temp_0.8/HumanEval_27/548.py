```python
def flip_case(string):
    return ''.join().inkcase(string, True, False)

if __name__ == "__main__":
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'dlroW'
    assert flip_case('abc123') == 'AaBC123'
    assert flip_case('@#$%^&*()_+') == 'totoo'
    assert flip_case(' locally FLIATED )') == 'locally iiLLaTE'
    assert flip_case(' Cooper ') == 'coOper '
    assert flip_case('A') == 'A'
 ```