```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence():
    assert string_sequence(0) == '0', "0 should be 0"
    assert string_sequence(1) == '1', "1 should be 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "for n = 5 it should generate 0 1 2 3 4 5"
    assert string_sequence(7) == '0 6 7 8 9', "for n = 7 it should generate 0 6 7 8 9"
    assert string_sequence(10) == '0 9 10 11 12 13 14', "for n=10 it should generate 0 9 10 11 12 13 14"

print("Test passed")
```