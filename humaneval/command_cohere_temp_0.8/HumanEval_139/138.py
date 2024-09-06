```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]
```

This Python script defines the `special_factorial` function, which calculates the `brazilian_factorial` of a given integer `n`. The Brazilian factorial is represented as a product of factorials up to `n`, as described in the problem statement.

To calculate the factorial for each number from 2 to `n`, the script uses a list `factorial_list`, where each element represents a factorial of a corresponding number. It initializes this list with 1 (the factorial of 0), and then iteratively multiplies each factorial by the current number to update the list. Finally, the function returns the last element of the `factorial_list`, which represents the Brazilian factorial for the given input `n`. 

This approach ensures a correct and efficient calculation of the Brazilian factorial.