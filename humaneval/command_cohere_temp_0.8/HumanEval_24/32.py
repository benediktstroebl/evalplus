```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            j = n // i  #Attendee
            if j > i:
                return j
            else:
                return i
```
The function largest_divisor iterates through numbers from 1 to n-1. Whenever it finds a number that divides n, it checks if any larger divisors exist by dividing n by this number (n / i). If the result is larger than the current number, it updates the variable j and returns it at the end. The loop continues until the largest divisor is found and returned.