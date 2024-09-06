```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer that evenly divides the given number."""
    # Verify if n is a prime
    if n == 2 or n == 3:
        return n
    elif n % 2 == 0:
        return 2
    else:
        for i in range(3,int(n**.5)+1,5):
            if n % i == 0:
                return i
        else:
            return int("non_integer_"+str(n))
```