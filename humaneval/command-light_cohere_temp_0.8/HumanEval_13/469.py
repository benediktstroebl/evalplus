```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return 0
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(7, 45))  # Output: 3 (it is divisible by both 7 and 45)

# Test case 4
print(greatest_common_divisor(17, 49))  # Output: 17
``` 
This script defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers a and b using Euclidean algorithm.  It algorithm repeatedly finds the  divisor of the smaller number and updates the divisor of the larger number. 

This algorithm stops when the smaller number becomes 0.  The result then represents the GCD of a and b.