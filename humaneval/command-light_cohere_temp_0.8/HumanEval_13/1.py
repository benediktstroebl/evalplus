```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    potential_divisors = [1]

    while b > 0:
        for divisor in potential_divisors:
            if a % divisor == 0:
                b //= divisor
                break
            potential_divisors.add(divisor,

    return max(potential_divisors)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```