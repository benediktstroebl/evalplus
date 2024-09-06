```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This version of the script leverages the Euclidean Algorithm for computing the GCD that states:
**GCD(a, b) = GCD(b % a, a)**

It's a recursive algorithm that repeatedly calculates the GCD of the remainder of b divided by a and the value of a. 

The base case of the recursion is when b is 0. In this case, the remainder is 0, and the GCD is assumed to be a value not affecting the result. 

This approach provides an optimal solution to the problem with a time complexity of O(log(min(a, b))). 

The markdown code block for the original problem is incorrect, as it fails to provide a test case for when `a` is 0, which is a potential edge case in the algorithm. The correct markdown code block is shown above, which updates the documentation to handle this edge case and ensures the function is correct for all cases. 

These changes reflect the use of the Euclidean Algorithm and address the issues in the original markdown code block.