```python
def fizz_buzz(n: int) -> int:
    result = 0
    for num in range(2, n+1):
        count = sum(i in str(num) for i in range(0, 9))
        if count % 2 == 0 and num % 11 == 0 or num % 13 == 0:
            result += 1
    return result
```