```python
def string_sequence(n: int) -> str:
    return f" {0:0>{n} "

if __name__ == "__main__":
    assert string_sequence(0) == '0', "0 not found"
    assert string_sequence(1) == '1', "1 not found"
    assert string_sequence(5) == '0 1 2 3 4 5', "5 not found"
    assert string_sequence(10) == "00 10 10 10", "10 not found"
```