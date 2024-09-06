```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(d for d in range(1, min(a, b)) + 1 if not a % d or b % d)

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This function calculates the greatest common divisor of two integers a and b, returning the result. It uses the efficient up by iterating through numbers from 1 up until it finds the first number that evenly divides both a and b without remainder.