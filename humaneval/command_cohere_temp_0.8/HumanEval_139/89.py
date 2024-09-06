```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` through `n!`. The core of the function iterates through integers from 2 to `n`, computing each factorial in the list using the previous factorial as the base, this is done `n+1` times, and each value is stored in the `factorial_list` list. Finally, the last element of this list, which represents the Brazilian factorial of `n`, is returned to the caller. 

The script's focus is on calculating the correct Brazilian factorial and providing an understandable implementation, it does not include built-in test cases, but it is ready to use for testing and computational purposes.