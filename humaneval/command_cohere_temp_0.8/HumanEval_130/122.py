```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [1] + [n//2] + tribonacci(n - 2)
    else:
        return [1] + tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n + 1)
```

The function uses a case-based approach to calculate the Tribonacci sequence, handling the base cases of `n=1` and `n=2` where the sequence is only one number, and using recursive logic to calculate the sequence for any other `n`. 

To follow the requirement of returning a list of the first `n + 1` numbers, the function returns a list for all cases, and the list will contain one number in the base cases, and the sequence of numbers for any other `n`.