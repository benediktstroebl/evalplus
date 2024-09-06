```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    potential_divisors = [1]

    while b != 0:
        if b % a == 0:
            potential_divisors.append(b)
        a = b
        b //=1

    return max(potential_divisors)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(7, 12))  # Output: 4 (correct result)
print(greatest_common_divisor(6, 18))  # Output: 6 (correct result)
```