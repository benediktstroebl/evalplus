```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence(n: int) -> None:
    assert len(string_sequence(n)) == n + 1, f"Length of sequence is not {n+1}"
    assert string_sequence(0) == "0", f"Start of sequence is not 0"
    assert string_sequence(n - 1) == "0", f"End of sequence is not 0"
    assert string_sequence(10) == "000010", f"Invalid sequence {n}."
```