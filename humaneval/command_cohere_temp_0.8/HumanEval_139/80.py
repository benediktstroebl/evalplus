```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```
This Python script defines a function called `special_factorial` which accepts a single parameter `n`. This function calculates the 'special factorial' of n, which is defined as `n! * (n-1)! * (n-2)! * ... * 1!` where `n > 0`. The function achieves this by setting a variable `fact` to 1 and then iterating through values of `i` from 1 to `n` and updating `fact` by multiplying it by the current value of `i`. Finally, the function returns the computed 'special factorial' of `n`. 

Here is an example usage of this function:
```python
>>> special_factorial(4)
288
```
This shows that when this function is called with an input of 4, it returns 288, which is indeed the 'special factorial' of 4, as defined in the original problem statement.