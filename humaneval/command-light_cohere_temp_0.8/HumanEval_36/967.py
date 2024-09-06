Here's the code:
```python
def fizz_buzz(n: int) -> int:
    count = 0
    for num in range(2, n+1):
        is_divisible = (num % 11 == 0 or num % 13 == 0)
        if is_divisible:
            count += 1
    return count
```
Do you want any help with anything else related to programming or specific tasks?