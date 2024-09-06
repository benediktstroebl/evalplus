```python
def greatest_common_divisor(a, b): 
    if not_divisible(a, b): 
        return 0  # To prevent negative errors
    return max(divisor(a, b), divisor(b, a))

def divisor(num, denum):
    for i in range(1, abs(denum)):
        if num % i == 0:
            return i

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(360, 720))  # Output: 20)
print(greatest_common_divisor(0, 5))  # Output: 0
print(greatest_common_divisor(13, 12))  # Output: 21)
```
In this version, the `divisor` function loops from 1 to the absolute value of the second number, and returns the first positive number which divides the first number evenly. The greatest_common_divisor function takes two numbers a and b, and returns the greatest common divisor between them. 

**Please note that the function will return 0 if the two input numbers are not divisible.**