```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    # Compute all divisors up to the square root of b
    limit = int(math.sqrt(b)) + 1
    divisors = []
    for num in range(1, limit):
        if a % num == 0:
            divisors.append(num)
            if b % (num**2) == 0:
                divisors.append((num**2))
                if a == 0 or b == 0:
                    return 0

    # Return the greatest divisor
    return max(divis, key=len)

# Example usage:
print(greatest_common_divisor(3, 5)) # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
 ```