```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return 4
    else:
        limit = int(math.sqrt(n)) + 1
        sqrt_n = int(math.sqrt(n))
        sequence = [0]
        for _ in range(limit):
            if sequence[-1] <= sqrt_n:
                sequence.append(2 * sequence[-1] + sequence[-2])
            else:
                sequence.append(sequence[-1] + sequence[-2]) + 1
        return sequence[n - 1]
```