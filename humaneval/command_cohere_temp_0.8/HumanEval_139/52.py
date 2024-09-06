```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```
This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` to `n!`. The function iteratively computes this list and returns the last element, representing the Brazilian factorial of `n`. The script ensures efficient computation of the Brazilian factorial and serves as a standalone solution to the problem statement.