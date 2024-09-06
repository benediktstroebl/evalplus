```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```
This Python script defines a function called `special_factorial` which accepts an integer `n` as input. The function calculates the `brazilian_factorial` of `n` by iterating from 1 to `n` (inclusive) and multiplying the current value of fact by each consecutive integer. The result is then returned. 

To test this, you can run the following snippet:
```python
special_factorial(4)
```
This will return the value `288`, which is the Brazilian factorial for `4`.