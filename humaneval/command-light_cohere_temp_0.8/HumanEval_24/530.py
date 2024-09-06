Here's the Python script with the function to find the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    l = 0
    while n % 2 == 0:
        l += 1
        n //= 2
    return 2*l + 1
```
This code defines a function `largest_divisor` that takes an integer `n` as input and finds the largest divisor of `n`. The function first checks if `n` is less than or equal to 1, and if so, returns `n`. Then, the function initializes a variable `l` to keep track of the largest divisor found so far. The function then checks if `n` is divisible by 2, by checking if the remainder of `n` divided by 2 is 0. The function then increments `l` and divides `n` by 2, effectively finding the next divisor. The function then returns the unique solution, the product of the largest divisor found and the count of divisors found so far.