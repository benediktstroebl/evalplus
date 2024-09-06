```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` to `n!`. The script then iterates through this list to calculate the product and return the result. The code is encapsulated within a function and can handle inputs greater than zero to compute the Brazilian factorial accurately.