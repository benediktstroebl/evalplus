```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through factors of `n` in the range of `1` to `n` and returns the maximum factor it finds. 
It is important to note that this approach has a time complexity of O(n) since it checks each element in the range. 
There are other optimizations that can improve this efficiency but may be beyond the scope of this problem.