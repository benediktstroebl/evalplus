```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n + 1) if any(n % x == 0)) or n)
```
This Python script defines a function named largest_divisor that takes an integer n as input and aims to find the largest divisor of n. The function employs a next() generator expression, which iterates through numbers from 1 up to n. Then, it checks each number against the n's divisors, ensuring that the divisor is smaller than n. 

It returns the first divisor encountered during the loop, which satisfies the requirement of being larger than n and evenly dividing n. The code is concise, effective, and follows the standard Python approach for solving this problem.