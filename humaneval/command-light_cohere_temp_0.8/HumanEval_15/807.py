Here is a self-contained Python script that defines a function string_sequence that solves the problem you described:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 1 {n+1} 2 {n+2} 3 {n+3} 4 {n+4} 5"

# Test the function with different inputs
test_cases = [0, 5, 10, 15]
for n in test_cases:
    print(string_sequence(n))
```