```python
def greatest_common_divisor(a, b): 
    while b != 0:
        if a % b == 0:
            a, b = b, a 
        else:
            b = divmod(b, a)
    return a
``` 
This function utilizes the Euclidean algorithm for finding the greatest common divisor of two integers a and b.