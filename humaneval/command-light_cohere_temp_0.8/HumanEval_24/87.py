Here's the provided Python script that implements the function `largest_divisor` with self-contained code:

```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if all(j == i%j for j in range(1, n+1)))
```

The function uses the `enumer` loop to iterate from 1 to the given number `n`. It then checks if the divisibility of each number in the range holds true by using the `all` function with the `range(1, n+1)` generator. The function returns the result when the number that satisfies this condition.