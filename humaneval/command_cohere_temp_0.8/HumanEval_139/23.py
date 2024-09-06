```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```
This Python script defines a function called `special_factorial` which accepts an integer `n` as input. The function calculates the `brazilian_factorial` of `n` by iterating through integers from 1 to `n` (both inclusive) and multiplying them together. This multiplication process effectively calculates the factorial of `n`, which is the result of multiplying together all positive integers from 1 to `n`. The function then returns this factorial as the "special factorial" for the given input `n`. 

For example, if `n` is 4, the function will compute the factorial of 4, which is 1 * 2 * 3 * 4 = 24.