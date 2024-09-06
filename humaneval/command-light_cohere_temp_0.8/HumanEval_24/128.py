```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), 0) or n
``` 
This function uses the Python `next` function with a generator expression to iterate through numbers from 1 to the user's number. The function then checks if the number is divisible by the current number using the condition `not n % d`. If a number is found that divides the user's number evenly (no remainder), then that number is returned.