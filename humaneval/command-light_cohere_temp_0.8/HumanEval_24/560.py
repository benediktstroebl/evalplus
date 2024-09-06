Here's a self-contained Python function that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number that divides n evenly, smaller than n."""
    while n % 2 == 0:
        n += 1
    return n
```
This function takes an integer n as input and uses a while loop to repeatedly increment n until it's even. At each increment, the function tests if n is divisible by 2. The loop continues until n becomes even. Once n is even even, the largest odd divisor of n (which is smaller than n) is returned.