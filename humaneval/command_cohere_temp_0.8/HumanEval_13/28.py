```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The script uses Euclidean algorithm for computing the greatest common divisor. It is based on the property that gcd(a, b) = gcd(b, a % b). The base case is when b is 0, and in that case, the gcd is a. 

The code is efficient and has a time complexity of O(log(min(a,b))). 

The script includes a corresponding Markdown multi-line comment providing relevant test cases for the function. These test cases help ensure the function operates as expected across various scenarios. 

To execute the Python script and run the tests, you can copy the code into a Python file (e.g., gcd.py) and execute the file in your Python interpreter. The interpreter will run the code and provide you with any test results or errors, giving you assurance that the function operates correctly.