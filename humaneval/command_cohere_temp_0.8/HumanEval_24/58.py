```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0 and n // i > i:
            return i
    return 1
```
The function iterates through numbers from 1 to n. If `n` is divisible by `i`, it checks if the divisor `i` is also the largest possible divisor, which would be `n // i`. If it is, it returns `i`. If not, it moves on to the next number in the iteration. The overall time complexity is O(d), where d is the number of digits in `n`.  This is because the for loop iterates through all numbers from 1 to n and performs operations on each.  Finally, the function returns 1 if no suitable divisor is found.