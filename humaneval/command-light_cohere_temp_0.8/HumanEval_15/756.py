```python
def string_sequence(n: int) -> str:
    return f" {0} {1} {2} {3} {4} {5}"[:n]

for i in range(0, 10):
    assert str(string_sequence(i)) == f" {i} {i+1} {i+2} {i+3} {i+4} {i+5}", "Test failed"
```