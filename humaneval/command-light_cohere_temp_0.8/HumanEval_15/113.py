Here is a self-contained Python script that defines a function `string_sequence`:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test case 1: Get sequence for n=0
assertEqual(string_sequence(0),'0')

# Test case 2: Get sequence for n=5
assertEqual(string_sequence(5),'0 1 2 3 4 5')

# Test case 3: Wheel of..
assertEqual(string_sequence(7),'0 6 7 8 9')
```

This script defines a function `string_sequence` that returns a string containing space-delimited numbers starting from 0 up to `n` (inclusive). The test cases provided then verify that the function is working correctly.