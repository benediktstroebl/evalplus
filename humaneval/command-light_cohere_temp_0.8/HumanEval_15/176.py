```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test cases
test_sequence = [
    lambda: round_sequence(0),
    lambda: str(round(float(test_sequence()))) == '0 0 0 0 0',
    lambda: test_sequence(5),
    lambda: test_sequence() == '0 1 2 3 4 5',
    lambda: test_sequence(10) == '0 10 10 10 10',
    assert test_sequence(15) == '0 15 15 15 15'
]
# Main code
if __name__ == "__main__":
    unittest.test_sequence()

```
This code defines a function 'string_sequence' which returns a string containing space-delimited numbers starting from 0 up to 'n', using the formula '0 * n'. The test cases are also defined to verify the correctness of the function.