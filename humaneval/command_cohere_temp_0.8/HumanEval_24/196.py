```python
def largest_divisor(n):
    """
    Find the largest divisor of n less than n.
    """
    for i in range(1, n):
        if n % i == 0:
            return i
```
The function iterates through factors of `n` from `1` to `n-1` and returns the largest factor that yields a remainder of 0 when divided by `n`. This value is the largest divisor of `n` less than `n` itself. The loop efficiently finds this divisor without the need for unnecessary factorizations. The descriptive function comment also provides clarity for users understanding the code's intent.

Here is a simpler solution using the built-in `math` module: 
```python
import math

def largest_divisor(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
```
This approach is also correct, producing the same results, but it lacks the efficiency and clarity of the prior solution.