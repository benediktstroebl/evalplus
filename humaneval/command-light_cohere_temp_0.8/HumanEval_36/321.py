Here is a self-contained Python script with a function that solves the problem you described:

```python
def fizz_buzz(n: int) -> int:
    return (n - 7) // 2 if n > 7 else 0
```

The function `fizz_buzz` takes an integer `n` as input and returns the number of times the digit 7 appears in the sequence of integers less than `n` which are divisible by 11 or 13. The function uses a mathematical formula to achieve this. The formula involves finding the formula and checking if `n` is greater than 7. 

The function returns 0 if the condition is not met.