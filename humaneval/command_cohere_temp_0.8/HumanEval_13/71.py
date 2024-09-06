```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This script defines a Python function called `greatest_common_divisor` that takes two integers a and b as input and returns the greatest common divisor of these two integers. The base case is detecting zero `a` and directly returning b. Otherwise, it recursively computes the GCD using the Euclidean algorithm, which is the remainder of b divided by a. 

Here is an example usage of this function:
```python
print(greatest_common_divisor(3, 5))  # 1
print(greatest_common_divisor(25, 15))  # 5
```
This will output:
```bash
1
5
```