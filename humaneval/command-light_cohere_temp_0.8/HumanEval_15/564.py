```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

for i in range(0,6):
    assert string_sequence(i) == f"0 {i}"*i
    print(f"Test passed for {i} ")
```