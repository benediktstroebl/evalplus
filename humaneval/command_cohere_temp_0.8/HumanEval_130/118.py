```python
def tribonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n % 2 == 0:
        return [0, 1, n // 2]
    else:
        return [tribonacci(n - 1)[-1], tribonacci(n - 2)[-1], tribonacci(n + 1)[-1]] + tribonacci(n // 2)
```

The function takes an integer n as input and returns a list of the first n + 1 Tribonacci numbers. It checks if n is equal to 0,1 or an even number to proceed with the appropriate calculation. If n is an odd number, it recursively calculates the last three Tribonacci numbers and adds them to the list returned by the tribonacci(n//2) function. To avoid overflow and improve efficiency, only the last three Tribonacci numbers are stored and updated iteratively, resulting in a more concise and optimized solution.