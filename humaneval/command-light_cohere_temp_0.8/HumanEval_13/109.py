```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input must be a number")
    return max(list(divisor(a, b)))

def divisor(x: int, y: int) -> int:
    if x == 0 or y == 0:
        raise ValueError("Both inputs must be positive numbers")
    while y % x == 0:
        x += 1
    return x
``` 
This code defines a function called `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b. It utilizes a multiple divisibility method and a helper function `divisor` to efficiently find the largest divisor of the difference between two numbers. 

This is a self-contained Python script that demonstrates how to solve the problem.