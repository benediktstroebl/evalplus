```python
def largest_divisor(n: int) -> int:
    return next( i for i in range(1, n+1) if any(n% i == 0))
``` 
This function employs the generator expression with the `range()` function and the `any()` function to generate all numbers from 1 up until the given number `n`. It then checks each number with the modulo operation `% n` to see if any of these numbers divide the given number evenly.