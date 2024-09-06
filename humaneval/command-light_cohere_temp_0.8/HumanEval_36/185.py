```python
def fizz_buzz(n: int) -> int:
    return len({d for d in range(10) if any(d % 11 == 0 or d % 13 == 0) and d == 7})
```
Now you can use this function in a markdown code block to get the result. The function is self-contained, and it uses list comprehension and the any function to check if any digit less than n is divisible by both 11 and 13.