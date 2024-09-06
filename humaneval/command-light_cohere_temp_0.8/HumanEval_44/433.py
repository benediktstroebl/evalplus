```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
        
    result = []
    while x >= 1:
        result.append( chr(ord('0') + x % base) )
        x //= base
    return ''.join(result) or '0'

# Unit tests
test_change_base = []
test_change_base.push(42)
test_change_base.push(48)
test_change_base.push(57)
test_change_base.push(97)
test_change_base.push(101)
test_change_base.push(105)
test_change_base.push(111)
test_change_base.push(153)
test_change_base.push(19)
test_change_base.push(57)

def test_func():
    for test in test_change_base:
        assert change_base(*test, 2) == '20'
        assert change_base(*test, 10) == str(test)

test_func()
```