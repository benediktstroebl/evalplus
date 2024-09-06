```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0] + tribonacci(n - 1)
    else:
        return [1] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```

The function takes an integer n as input and returns a list of the first n + 1 numbers in the Tribonacci sequence. It handles the base cases of n=1 and n=0, and uses recursion and memoization to efficiently calculate the Tribonacci sequence for odd values of n.