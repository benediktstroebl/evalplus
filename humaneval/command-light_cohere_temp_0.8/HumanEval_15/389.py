```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)
    """
    Test:
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'
    assert string_sequence(2) == '0 2'
    assert string_sequence(3) == '0 1 2'
    assert string_sequence(4) == '0 2 4'
    assert string_sequence(6) == '0 3 6'
    assert string_sequence(7) == '0 3 6 7'
    assert string_sequence(15) == '0 14 13 12 11 10 8 7 6 5 3 2'
    """