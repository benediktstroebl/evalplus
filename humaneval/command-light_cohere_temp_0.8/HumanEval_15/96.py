```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}..."

for _ in range(10):
    assert string_sequence(int) == f"0 {_ + 1}".format(int)
```