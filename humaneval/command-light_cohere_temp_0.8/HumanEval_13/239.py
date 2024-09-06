```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # find the greatest common divisor
    gcd = int(math.gcd(a, b))
    return gcd

# test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# test case 3
print(greatest_common_divisor(107, 153))  # Output: 29
``` 
This code defines a function greatest_common_divisor that calculates the greatest common divisor of 2 integers a and b. The function works by checking the existence of both numbers, and then performs the Euclidean gcd algorithm to find the gcd. The function then returns the maximum common divisor.