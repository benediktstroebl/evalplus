```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if not n % i)
```
The function uses the list comprehension technique to test if any number greater than one divides the input number n evenly. It starts from i = 1 and checks each integer till it reaches n. This method is unique approach that uses the `next()` function to iterate over the numbers without needing to specify an explicit range.