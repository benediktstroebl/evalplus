```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. It initializes a list `factorial_list` with values of factorials from 1! to n!. Then, it calculates the factorial of n by multiplying `n!` with the `(n-1)!` value from the list, updating the list in place, and this process continues for all values from `n-1` down to 2. Finally, it returns the factorial of n, which is the value of `factorial_list[n]`. 

The script ensures efficient calculation and retrieval of factorial values up to `n` without recalculating intermediate factorials. It addresses the problem in a direct and understandable manner, avoiding complex recursive implementations.