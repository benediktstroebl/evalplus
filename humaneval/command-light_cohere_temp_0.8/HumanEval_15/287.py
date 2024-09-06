```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."

for _ in range(10):
    assert_equals(string_sequence(int), f"0 {int}..."), f"Got {_}- expected 0 {int}...\n")
    assert_equals(string_sequence(int)(int), f"1 {int}..."), f"Got {_}- expected 1 {int}...\n")
    assert_equals(string_sequence(int)(int)(int), f"2 {int}...", f"Got {_}- expected 2 {int}...\n")
    assert_equals(string_sequence(int)(int)(int)(int), f"3 {int}...", f"Got {_}- expected 3 {int}...\n")
    assert_equals(string_sequence(int)(int)(int)(int)(int), f"4 {int}...", f"Got {_}- expected 4 {int}...\n")
    assert_equals(string_sequence(int)(int)(int)(int)(int)(int), f"5 {int}...")
```