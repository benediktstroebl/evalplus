```python
def string_sequence(n: int) -> str:
    if n < 0:
        raise ValueError("n must be a positive integer")
    return f"0 {n}".join(str(i) for i in range(1, n+1))

def test_string_sequence():
    try:
        result = string_sequence(5)
        assert result == '0 1 2 3 4 5'
        return
    except AssertionError as e:
        print(f"Error: {e}")
```
Do you need assistance with any other code related tasks?