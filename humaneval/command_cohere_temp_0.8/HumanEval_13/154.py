```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a function called `greatest_common_divisor` that takes two integers a and b as input and returns the greatest common divisor of these two integers. The base case of the recursion is b == 0, in which case the function returns a. The recursive case is when b is not 0, in which case the function returns the gcd of b and the remainder of a divided by b (a % b). This aligns with the definition of a gcd as the largest integer that divides both a and b without a remainder. 

Here is an example usage of this function:
```python
result = greatest_common_divisor(10, 15)
print(result)  # Output: 5
```
This will print the greatest common divisor of 10 and 15, which is 5. 

This approach leverages the beauty of dynamic programming through recursion to solve this problem efficiently in polynomial time.