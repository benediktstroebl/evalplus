```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3} {n+4}"

def test_sequence(test_cases: list[int]) -> None:
    assert test_cases == [0,1,2,3,4,5], f"Test passed: {test_cases}"
    for n in test_cases:
        assert str(string_sequence(n)) == f"0 {n} {n+1} {n+2} {n+3} {n+4}", f"Test failed: {n}"

# Example usage
test_sequence([0,5])
```