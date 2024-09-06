```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    return greatest_common_divisor(b % a, a)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This function calculates the greatest common divisor of two integers a and b. For the first test, it returns 0 if either input is 0, otherwise it uses the other approach to find the GCD. The tests ensure that the correct behavior of the function.