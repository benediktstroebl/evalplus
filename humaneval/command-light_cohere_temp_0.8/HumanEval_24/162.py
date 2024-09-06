```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number divisible by n, 
    ensuring it's less than n.
    """
   
    if n <= 0:
        return 0
    divs = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divs.push(i)
    largest = max(divs)
    return largest
```