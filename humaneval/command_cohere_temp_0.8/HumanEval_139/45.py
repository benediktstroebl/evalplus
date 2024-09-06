```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```
This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` through `n!`, where each factorial is the product of all positive integers up to its index.

The code generates this factorial list incrementally, starting with `1!` and multiplying each factorial by `i` to get the next value in the list. To compute the Brazilian factorial for a specific value of `n`, the function retrieves the `n`-th element from this pre-calculated factorial list and returns it. This method is highly efficient, as it requires only a single list iteration to calculate, making it optimized for responsiveness.