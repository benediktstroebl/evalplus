```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    m = max(abs(a), abs(b))
    return max([d for d in range(1, m) if a % d == 0 and b % d == 0])

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This Python function calculates the greatest common divisor of two integers a and b. The function returns the value of the greatest common divisor, which is the largest integer that evenly divides both a and b without leaving a remainder. The function handles the scenarios such where one or both numbers are 0, as well as where one or both numbers are large relative to each other, it uses the max function to find the larger of the absolute values of a and b, and then iterates through the range of positive integers less than the larger value, checking if both a and b are divisible by d. The function then returns the value of the greatest common divisor.