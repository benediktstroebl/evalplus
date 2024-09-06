```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number that divides n evenly, smaller than n"""
    return next((d for d in range(1, n+1) if n % d == 0))
``` 
This function uses the list comprehension to generate numbers from 1 to n, then checks if there's a number in that list that evenly divides n. 
The use of next to avoid an infinite loop, and returns the first such number.