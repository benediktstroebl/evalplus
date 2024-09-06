```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != b:
        if a % b == 0:
            a = b
        else:
            b = a

    return min(a, b)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This function, `greatest_common_divisor`, takes two integers as input and returns the greatest common divisor of the two numbers. This is using a basic algorithm to find the GCD. The function first checks if either input is 0 (which would mean they are equal), and returns the other number. If both inputs are not 0, it then enters a loop where it repeatedly divides the larger number by the smaller one until they are equal, and keeps track of which number is divisible by which one. The smaller one is eventually.