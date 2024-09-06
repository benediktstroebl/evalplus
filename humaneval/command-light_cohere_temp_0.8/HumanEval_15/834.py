Here is a Python script that contains a self-contained function that generates a sequence of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

for i in range(0, 6):
    assert string_sequence(i) == f"0 {i}",f"Expected {i} but got {str(i)} instead"
```