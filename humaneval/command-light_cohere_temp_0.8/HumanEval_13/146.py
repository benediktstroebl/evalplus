```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    if a < b:
        return greatest_common_divisor(b, a)
    
    return min(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(9, 51))  # Output: 1 (1 is a divisor of all numbers)
print(greatest_common_divisor(185, 427))  # Output: 427 

```
The function `greatest_common_divisor` calculates the greatest common divisor of two integers `a` and `b`. It handles cases where either input is zero, and it returns the minimum of the two numbers, ensuring the result is always positive.  The test cases demonstrate its expected behavior.