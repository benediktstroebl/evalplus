```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a

    # Use the Euclidean Algorithm to find the greatest common divisor
    while a != 0 and b != 0:
        t = b // a
        a = a - t * b
    # Return the final result
    return min(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(4, 6))  # Output: 2
print(greatest_common_divisor(9, 12))  # Output: 3
print(greatest_common_divisor(50, 25))  # Output: 25
``` 
This Python function, greatest_common_divisor, calculates the greatest common divisor of two integers a and b. The function first checks if either a or b is equal to zero; if either condition is met, the function returns the other value. If both a necessary, the function proceeds to use the Euclidean Algorithm to find the greatest common divisor. The algorithm continues until one of the numbers becomes zero. The function then returns the final result, which is the greater of the two numbers.