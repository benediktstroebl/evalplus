```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}"
    
def test_sequence(self, n: int) -> None:
    assert len(self.string_sequence(n)) == n + 1, f"Error: Length is not {n+1}, it should be {n}"
    assert any(c.isdigit() for c in self.string_sequence(n)), f"Error: Non-digit character found in the output: {c}"
    assert self.string_sequence(n) == f"0 {n}{' ' * (n - 1)}", f"Error: {self.string_sequence}n't be equal to the output"

```