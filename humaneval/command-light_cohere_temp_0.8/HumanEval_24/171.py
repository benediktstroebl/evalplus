```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
``` 
This function uses the list comprehension with the range function to generate numbers from 1 up to the input number. It then checks if the results are divisors of n, by checking if the input number is divisible by each number with an integer division result of 0.