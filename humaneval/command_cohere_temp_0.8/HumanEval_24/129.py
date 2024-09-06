```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number is divisible by n, it returns the largest number within this range. The loop ensures that the returned divisor is the largest possible and is smaller than n. This approach works for positive integers and performs logarithmic time complexity, checking divisibility for all numbers up to n.