```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test cases
test_cases = [
    15, 
    10,
    7,
    8,
    9,
    6,
    5,
    4,
    3
]

for i, n in enumerate(test_cases):
    print(f"Case {i+1}: {n} {largest_divisor(n)}")
```