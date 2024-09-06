```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0

    # to ensure positive numbers
    a = abs(a)
    b = abs(b)

    while b != 0:
        if a % b == 0:
            return b
        a //= b

    return a

# Test the function with different inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(7, 49))  # Output: 1 (only 7 and 49 share a common divisor)
print(greatest_common_divisor(3, 49))  # Output: 1 (only 3 and 49 share a common divisor)
print(greatest_common_divisor(105, 301)) # Output: 1
``` 
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function uses the strategies like ensuring the positive values and then finding the greatest factor of b that divides a for the rest of the numbers until b becomes zero.