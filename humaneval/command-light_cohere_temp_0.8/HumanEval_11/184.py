```python
import stringtypes

def string_xor(a: stringtypes.str, b: stringtypes.str) -> ->:"
Passes: a is str and b is str
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert len(a) == len(b)
    assert all(isinstance(c, int) for c in a) and all(isinstance(c, int) for c in b))
    assert a ^ b == '100'
```