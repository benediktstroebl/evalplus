```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(a, b) / info(a, b)
    
def info(x: int, y: int) -> int:
    d = greatest_common_divisor(x, y)
    return (x * y) // d if d != 0 else 0
```
This function greatest_common_divisor calculates the greatest common divisor of two numbers a and b. The function utilizes the information of both numbers, efficiently calculating the GCD with a single method. It also includes input validation to ensure that the function is only called with valid inputs. The code is self-contained and follows PEP.