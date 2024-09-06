```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    d1 = divisor(a)
    d2 = divisor(b)
    
    if d1 == d2:
        return d1
    elif d1 > d2:
        return d1
    else:
        return d2

def divisor(num):
    limit = int(math.sqrt(num) + 0.0)
    result = []
    for i in range(1, limit):
        if num % i == 0:
            result.append(i)
    return result
```
This Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers `a` and `b`. The function uses a helper function `divisor` to efficiently find divisors of the input number `num`. The `divisor` function iterates up to the square root of the input number, checking for divisibility and storing the divisors in a list. Then, the `greatest_common_divisor` function compares the divisors of `a` and `b` and returns the greater divisor, or 0 if they are equal.  This maximum common divisor of `a` and `b` is the greatest divisor of the list of divisors.