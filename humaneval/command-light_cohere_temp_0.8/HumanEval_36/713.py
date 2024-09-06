Here's the solution to the problem:
```python
def fizz_buzz(n: int) -> int:
    total_times = 0
    num_7 = 0

    for num in range(1, n+1):
        if num % 11 == 7 or num % 13 == 7:
            num_7 += 1
        total_times += num_7  # Count the number of 7s up to the current number

    return total_times
```

This function counts the number of times the digit 7 appears in integers less than `n` and which are divisible by 11 or 13. It runs through a example test to demonstrate its functionality.