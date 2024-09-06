Here's a self-contained Python script that defines a function `greatest_common_divisor` solving the problem of finding the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided")
    return max(a, b) / min(a, b) if min(a, b) != 0 else 0

# Test cases
test_ GreatestCommonDivisor = """
import random

numbers = [5, 2]
for test_num in numbers:
    print(random.randint(1, 10) for x in range(test_num))
print(greatest_common_divisor(random.randint(1, 10), random.randint(1, 10)))
"""

test_ GreatestCommonDivisor
```