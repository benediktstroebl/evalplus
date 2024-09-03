```python
def simplify(x, n):
    x = x.replace()  #.split(x = 'frac', x)
    if x[0] * n == 0:
        return True
    return False

# Test cases
test_cases = [
    ("1/5", "5"),
    ("7/10", "10"),
    ("1/6", "2"),
    ("5/2", "2"),
    ("1/4", "2"),
    ("3/8", "2")
]

# Test function
for x, n in test_cases:
    result = simplify(x, n)
    print(f"{x} * {n} should be {result}")
```