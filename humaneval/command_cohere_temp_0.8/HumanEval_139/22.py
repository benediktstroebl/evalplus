```python
def special_factorial(n):
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i - 1])
    return factorial_list[n]
```
This Python script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. The function iteratively calculates the factorials of integers from 2 to n, creating a list of factorials. Then, it returns the last value in this list, which is the Brazilian factorial of the input integer `n`. This approach efficiently computes the result and ensures accuracy.