```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as arguments and returns the greatest common divisor of the two numbers. The base case of the recursion is b == 0, where the function returns a. The recursive case returns the gcd(b, a % b), which is the greatest common divisor of b and the remainder of a divided by b (a % b). 

Here is an example usage of the function:
```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```
This passes the test cases provided. It is worth noting that the time complexity of this function is O(log(min(a,b))). If the inputs are very large, this can be inefficient. 

Would you like to optimize this function further or discuss different testing strategies? Feel free to ask for refactoring advice or any specific concerns you have about your code.