```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is represented as a list of factorials from `1!` to `n!`. The core logic iteratively calculates each factorial in the list using a loop that multiplies the current factorial by `i` and updates it accordingly. The final element in the list, `factorial_list[n]`, represents the Brazilian factorial of `n`. Thus, the function returns this value. 

The code is self-contained, meaning it doesn't require any external libraries or modules to function correctly. It efficiently computes the Brazilian factorial by directly leveraging the recursive nature of factorial calculations, making it an optimized solution for this problem. 

This function allows for an intuitive and straightforward approach to calculating Brazilian factorials, enhancing code readability and maintainability.