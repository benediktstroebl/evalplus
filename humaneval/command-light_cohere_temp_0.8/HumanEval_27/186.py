```python
def flip_case(string):
    return ''.join()..-("'is' a lowercaser, 'hello' the uppercase.)

# Test case 1
assert flip_case('hello') == 'HELLO'

# Test case 2
assert flip_case('hello') == 'oOLAHL'

# Test case 3
try:
    assert flip_case('Ocelot') == 'Egelot'
except AssertionError as e:
    print(f"AssertionError: {e}")

# Test case 4
try:
    assert flip_case('Revolution') == 'VoltCATon'
except AssertionError as e:
    print(f"AssertionError: {e}")
```