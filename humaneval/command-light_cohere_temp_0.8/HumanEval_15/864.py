```python
def string_sequence(n: int) -> str:
    return f"0 {n} ".format(n)

for i in range(10):
    assert string_sequence(i) == f"0 {i}", f"Expected 0 {i}, got {str(i)}"

print("Test passed!")
```