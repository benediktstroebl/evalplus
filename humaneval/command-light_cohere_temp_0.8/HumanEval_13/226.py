```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)
# tests
print(greatest_common_divisor(3, 5))  # 1
print(greatest_common_divisor(25, 15)))  # 5
```  This code defines a function greatest_common_divisor that calculates the greatest common divisor of two integers a and b. This algorithm uses recursion and the strategy of calling itself with the arguments (b, a%b) to calculate the GCD of those numbers. 

Note that this solution is self-contained and does not require any additional variables outside the function.