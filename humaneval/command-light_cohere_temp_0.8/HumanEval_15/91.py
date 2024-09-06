```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2} {n+3}"
    
def test_string_sequence(test_cases: list) -> None:
    for test in test_cases:
        assert string_sequence(test) == test
        print("All tests passed!")
# Example test cases
test_cases = [0, 5]
test_string_sequence(test_cases)
 ```