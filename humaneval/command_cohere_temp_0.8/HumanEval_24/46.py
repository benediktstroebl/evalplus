```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number at index `i` divides `n` evenly (i.e., `n / i` is a whole number), the function returns `i`. This assumes that there is at least one number less than or equal to `n` that divides `n` evenly. This assumption holds true for all positive integers and is a key property of integers in mathematics.  If there is a tie between multiple numbers that are equally large and divisible, the function returns the smallest as specified by the problem definition, as it's the largest divisor that is smaller than n.