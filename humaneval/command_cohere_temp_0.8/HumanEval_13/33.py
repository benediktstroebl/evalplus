```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a function `greatest_common_divisor` that finds the greatest common divisor of two integers a and b. It repeatedly calls this function with `b` and the remainder of a divided by b until b is zero. It returns a if b is zero, which ensures that a divide-by-zero error does not occur. This algorithm is known as the Euclidean algorithm, and it is a standard approach for computing the GCD of two numbers. 
Here is a simple test case to verify its functionality:
```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
>>> greatest_common_divisor(1, 2)
1
``` 
This produces the expected output of 1, confirming that the function works as intended.