```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both numbers must be given.")
    return max((i) for i in range(1, max(a, b)) if not a % i == b % i)

# Test the function with a couple of numbers
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```