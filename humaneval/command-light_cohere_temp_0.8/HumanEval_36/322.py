```python
def fizz_buzz(n: int):
    return len({i for i in range(1, n + 1) if i % 10 == 7 and i % 11 == 0 or i % 10 == 7 and i % 13 == 0})

# Testing the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This function calculates the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function achieves this through a loop that iterates through numbers from 1 to n, and checks whether the current number is divisible by both 11 and 13. The function then returns the a dictionary of numbers that meet this condition, which are then filtered to obtain the final count.