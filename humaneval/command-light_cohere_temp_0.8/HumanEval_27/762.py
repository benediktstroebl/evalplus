```python
def flip_case(string):
    return ''.joinnlowercase(string.split()[0]) if ''.lower() else ''.upper()

# Tests
assert flip_case('hello') == 'HELLO'
assert flip_case('HEllO') =='oELLo'
```