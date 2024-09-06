```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This algorithm utilizes Euclid's Algorithm implicitely: it Continues subtracting the smaller number from the larger number and taking the remainder, until the remainder is smaller than the original smaller number.
It repeatedly divides the larger number by the smaller number and returns the smaller of the two, until the smaller number becomes zero. 
At each step, the remainder becomes the new smaller number, and the larger number is updated to the remainder divided by the smaller number. 
This algorithm is very efficient, and its runtime is O(log(min(a,b))). 
This algorithm is simpler and faster than doing a direct division and taking the GCD, especially for large numbers. 
Also, GCD of two numbers 'a' and 'b' is equal to GCD of 'b' and 'a% b', hence the recursive call with rest paraments (b, a % b). 
It is also worth noting that the GCD of 0 and any number is the any number since any number divides 0, hence the special case of b == 0. In the case of b == 0, the algorithm returns a without any recursive call. 
This approach does not require a import statements and is self contained. 
The function should work properly for any integers 'a' and 'b'. 
It will not work for non-integer types, but that is consistent with Python's type inference on the function signature.  if b == 0:
    return a 
return greatest_common_divisor(b, a % b) 
```