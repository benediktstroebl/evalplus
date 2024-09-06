```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It exploits the fact that the greatest common divisor remains the same when dividing by a larger number. Starting with the larger number, it repeatedly divides one number by the other, reducing the smaller number until it reaches zero. The divisor throughout the process is the GCD. 

It's a self-contained script that defines the function `greatest_common_divisor`, which takes two integers a and b as input and returns the greatest common divisor of a and b. 

Here is an example of how you can use the function:
```python
result = greatest_common_divisor(10, 15)
print(result)  # 5
```
This will print 5, which is the greatest common divisor of 10 and 15. 

The function works for any two integers a and b and is not limited to positive integers. It can also handle negative numbers, zeros, and floats. 

The time complexity of the algorithm is O(log(min(a,b))). This is much faster than calculating the GCD using a loop, which would have a time complexity of O(n).