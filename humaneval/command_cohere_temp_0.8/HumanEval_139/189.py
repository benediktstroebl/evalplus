```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem. It initializes a list `factorial_list` with values of factorials from 1! to n!. Then, it computes the `factorial_list` iteratively, where each element at index `i` is computed as `i * factorial_list[i - 1]`. Finally, it returns the value of `factorial_list[n]`, which is the Brazilian factorial of `n`. 

The code is self-contained and does not rely on any external variables or functions, making it easy to use and integrate into other projects.