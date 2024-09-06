Here is a self-contained Python function that finds the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    l = 0
    while n % l == 0 and l <= n // 2:
        l += 1
    return l
```
This function, `largest_divisor`, takes an integer `n` as input and returns the largest integer that divides `n` evenly, smaller than or equal to `n`. It uses a `while loop` to iterate through divisors less than or equal to the square root of `n`. 

Please note that the function uses the condition `n % l == 0` to check if `l` is a divisor of `n`, and increments `l` if it is.

This code is self-contained because it does not rely on the input `n` to calculate the largest divisor.  Instead, it uses a recursive approach to find the largest divisor, while checking divisibility.  This can be tested using a number `n` as input, and can be used in other functions or programs.