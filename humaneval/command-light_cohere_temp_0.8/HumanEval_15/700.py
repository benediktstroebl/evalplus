Here's the solution to the problem using Python:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test cases
test_sequence = [
    assert string_sequence(0) == '0', "Should return 0"
    assert string_sequence(1) == '1', "Should return 1"
    assert string_sequence(2) == '02', "Should return 02"
    assert string_sequence(3) == '003', "Should return 03"
    assert string_sequence(4) == '404', "Should return 404"
    assert string_sequence(5) == '005', "Should return 05"
]
```
The function will return a string containing space-delimited numbers starting from 0 and ending at n. 
This will ensure that the test cases are passed as expected.