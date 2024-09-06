```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0
    elif a == b:
        return a
    else:
        return greatest_common_divisor(b%a, a) + 1
``` 
This function calculates the greatest common divisor (GCD) of two integers a and b. By using the use a recursion, which is a common technique to solve this problem efficiently.