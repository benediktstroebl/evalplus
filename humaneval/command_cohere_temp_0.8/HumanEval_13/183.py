```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This code defines a Python function called `greatest_common_divisor` which takes two integers a and b as input. It is a recursive algorithm that utilizes the Euclidean algorithm to find the greatest common divisor (GCD) of the two numbers.

Here is an example of how to use this function:
```python
print(greatest_common_divisor(16, 36))  # Output: 4
```
This will return 4, which is the greatest common divisor of 16 and 36.