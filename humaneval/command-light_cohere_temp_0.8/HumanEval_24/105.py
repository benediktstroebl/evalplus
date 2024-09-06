Here is a Python script with a self-contained function that solves the problem of finding the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    result = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            result = i
    return result
#Test case:
print(largest_divisor(15))  # Output: 5
``` 
This script provides a function `largest_divisor` that takes an integer n as input and returns the largest integer which divides the number evenly, smaller than or equal to the given number.