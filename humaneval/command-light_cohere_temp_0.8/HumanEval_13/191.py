```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    max_div = 0
    for i in range(1, min(int(a**0.5)+1, b+1)+1):
        if a % i == 0 and b % i == 0:
            max_div = max(max_div, i)

    return max_div
``` 
This code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. The function first checks if either input is `None` and returns 0 in such case. It then iterates through loop from 1 to the minimum value of the sum of the squares of the two input numbers, adding the smallest common divisor encountered so far to the `max_div` variable. The loop continues until it value of `a` or `b` exceeds the sum of their squares plus one. 

This is a self-contained Python function that provides a clear and concise way to solve this problem.