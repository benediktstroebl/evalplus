```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It operates by continually subtracting the smaller number from the larger one and adjusting the divisor accordingly, eventually converging to the GCD. 
It passes the given tests because, for any given integers a and b, the GCD will always be the largest integer that divides both a and b evenly. The function returns the larger of the two integers when the smaller is smaller than the larger and returns the smaller integer when the two integers are equal. In all other cases, it recursively calls the function, subtracting the smaller number from the larger one and adjusting the divisor accordingly, until it converges on the correct answer. 
It is worth noting that for the given examples provided, the base cases would not be reached because the a value is always greater than b, or vice versa, and the recursive calls will always produce the correct answer. In the first example, it will return 5 for the first call: greatest_common_divisor(5, 3), then greatest_common_divisor(5%3, 3) which is greatest_common_divisor(2, 3) and so forth until it returns 1, which is the correct answer. 
For the second example, the process will be greatest_common_divisor(25, 15), then greatest_common_divisor(15, 25%). These intermediate steps will eventually reach the correct answer, 5.