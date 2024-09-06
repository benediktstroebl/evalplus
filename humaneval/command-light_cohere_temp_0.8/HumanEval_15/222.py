```python
def string_sequence(n: int) -> str:
    return f"0 {n} 1 {n+1} 2 {n+2} 3 {n+3} 4 {n+4}"

def test_string_sequence(test_cases):
    assert test_cases == ["0", "1", "2", "3", "4", "5"]

# Driver code
test_string_sequence(5)
```