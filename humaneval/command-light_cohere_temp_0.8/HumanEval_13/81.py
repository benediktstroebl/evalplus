```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is not a number")
    return max(divisor(a) for divisor in divisors(b))

def divisors(n):
    yield [1,  n]
    for i in range(1, n//2 + 1):
        yield n // i

test_greater_common_divisor = [
    (3, 5),
    (25, 15),
    ]

for test in test_greater_common_divisor:
    print(greatest_common_divisor(*test))
```