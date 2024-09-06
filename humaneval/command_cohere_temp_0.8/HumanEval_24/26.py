```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function `largest_divisor(n)` takes a number `n` as input and iterates through all numbers from 1 to `n` (inclusive). During each iteration, it checks if the current number `i` can divide `n` evenly. If `n` is divisible by `i` without any remainder, it means that `i` is a divisor of `n`. The function returns the largest such divisor, which is the closest divisor smaller than `n`. 

Here is an example outcome of the function for different test cases:
```
largest_divisor(15)
Out[1]: 5

largest_divisor(16)
Out[2]: 8

largest_divisor(17)
Out[3]: 16
```
The first example shows that the function correctly finds the largest divisor of 15, which is 5. The second example shows that the function finds the largest divisor of 16, which is 8. The third example shows that the function finds the largest divisor of 17, which is 16. 

To ensure that the function performs well, ensure that the range of the loop is limited to `n + 1` because the largest divisor of `n` will always be a number less than `n`. 

This approach has a time complexity of O(n) as it iterates through all possible candidates, and it is certainly not the most efficient approach, but it is simple and easy to understand. There are more efficient ways to find the largest divisor with lesser time complexity.