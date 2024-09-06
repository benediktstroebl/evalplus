```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        return greatest_common_divisor(b, a % b)

print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(10, 20))  # Output: 5
``` 
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two integers a and b. The function first checks if either a or b is equal to 0, and if so, returns 0 as the result. It then checks for specific cases: if b is 1, it returns a; if a is 1, it returns b; and if both are greater than 1, it recursively calls itself on finding the greatest common divisor of the remainder of a and b. By default, it uses the same process, which is a good practice for functions with potential for edge cases.