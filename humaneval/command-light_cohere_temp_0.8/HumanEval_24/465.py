```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), -1)
```
This function uses the Python next() function with a generator expression to iterate through the numbers from 1 up to the input number n. The function returns the per the a list comprehension checks if the current number d divides the input number n evenly (i. If it does, it returns -1, indicating that no larger number than n divides evenly into n.