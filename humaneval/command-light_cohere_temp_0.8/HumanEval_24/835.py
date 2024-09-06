```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
```
This Python code defines a function named largest_divisor, which takes an integer n as input and returns the largest integer that evenly divides into n. The function achieves this using a list comprehension, where it generates all numbers from 1 up to n and checks if the number does not divide n evenly (i. The "next" function is used to iterate over the list of divisors. This way is most the interesting and efficient way to find the largest divisor for a given number.