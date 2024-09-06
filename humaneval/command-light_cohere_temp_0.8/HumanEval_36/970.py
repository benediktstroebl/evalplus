```python
def fizz_buzz(n):
    num_seven = 0
    for i in range(1, n+1):
        num_seven += (i % 11 == 7) or (i % 13 == 7)
    return num_seven
```

This function uses a loop to iterate through numbers less than n. It then checks if the the condition (i % 11 == 7) or (i % 13 == 7). The function returns the number of times the number 7 appears in the sequence of integers less than n which are divisible by 11 or 13.