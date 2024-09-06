```python
def flip_case(string):
    return ''.join(''.lower() if c.isalpha(ord(c)) else c for c in string)

# Test cases
assert flip_case('hello') == 'HELLO'
assert flip_case('HEllO') == 'hello'
assert flip_case('o
											rthy') == 'oryH'
assert flip_case('To​BeOrNot') == 'BEnoNot'
assert flip_case('the quick brown fox jumps over the lazy dog') == 'TheQuickBrownFoxJumpsOverTheLazyDog'
```