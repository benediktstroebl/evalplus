```python
def string_sequence(n: int) -> str:
    return f"0 {n}..."
    # tests:
    assert len(string_sequence(0)) == 1
    assert len(string_sequence(1)) == 3
    assert len(string_sequence(5)) == 5
    assert string_sequence(10) == "0010" # should output 10 20 30 40 50 ..."
    assert string_sequence(0) == "0" + "0" * n for n in range(1, 10)
    assert string_sequence(6) == "0 60" # should output 0 60 180 240 ...
    assert string_sequence(10) == "001010101010101"
```