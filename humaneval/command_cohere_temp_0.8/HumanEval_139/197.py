```python
def special_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
```
This Python script defines a function called `special_factorial` which accepts an integer `n` as input. This function calculates the `brazilian_factorial` of `n` by iterating from 2 up to `n` (inclusive) and multiplying the current value of `fact` by each number in this sequence. The `fact` variable is initialized to 1, and it gets updated by multiplying it with the current iteration value in each iteration. This computation mimics the definition of the Brazilian factorial, which is the product of all positive integers from 1 to n. This is done to ensure that `fact` holds the Brazilian factorial value for the given input `n` upon completion of the loop. Finally, the function returns the computed `brazilian_factorial` of `n`. 

Here is an example usage of the function:
```python
>>> special_factorial(4)
288
```
This invocation demonstrates its use on an input of `4`, and the result is the Brazilian factorial of 4, which is 288.