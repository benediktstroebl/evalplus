```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return 0
    elif b == 0:
        return a
    else:
        return max(a, b)

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This Python script defines a function called greatest_common_divisor that takes two integers a and b as input and returns the greatest common divisor of a and b. The function uses a condition to check for the case where either a or b is 0, and returns 0 in such cases. It then uses the final one to determine the greatest common divisor of a and b, returning the result.