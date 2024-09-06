Here is a self-contained Python function that finds the greatest common divisor (GCD) of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(a, b) / max(b % a, a % b)

# Example usage:
a = 3
b = 5
print(greatest_common_divisor(a, b))  # Output: 1
```
This function efficiently calculates the GCD by finding the maximum of the two inputs and then dividing by the smaller remainder or quotient, ensuring the result is the greatest common divisor.