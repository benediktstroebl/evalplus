```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive approach is quite efficient and decreases the size of the problem with each iteration. It is based on the idea that to find the GCD of a and b, we can just find the GCD of b and a % b. This process continues until b is 0, at which point the GCD is found to be a. 
This approach is quite efficient because the size of the problem is reduced with each recursive call. The time complexity of this approach is O(log(min(a, b))). 
The recursion will continue as long as b is not 0, in some cases where a is also 0, the function will not terminate, this can be adjusted with a base case `if a == 0: return b` for better clarity and precision. Familiarize yourself with recursion and its mechanics before implementing it in your code to prevent any issues or bugs. 
If you wish to optimize the function and improve its efficiency even further you may consider implementing the Euclidean Algorithm optimized version `https://en.wikipedia.org/wiki/ Euclidean_algorithm#Optimized_version`.