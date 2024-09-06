```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` through `n!`.

The code initially creates a list, `factorial_list`, with a `1!` element. It then iterates through integers ranging from `2` to `n`, multiplying each integer by the previous factorial and adding it to `factorial_list`. This builds a proper list of factorials.

Finally, the function returns `factorial_list[n]`, which is the Brazilian factorial of `n`. 

This approach efficiently calculates the Brazilian factorial, making it an optimized solution for the problem.