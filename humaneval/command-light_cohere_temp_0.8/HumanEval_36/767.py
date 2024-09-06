Here's the solution:
```python
def fizz_buzz(n: int) -> int:
    count = 0
    for num in range(10, n + 1):
        if ( num % 11 == 0 or num % 13 == 0 ):
            count += 1
    return count
```
Do you want me to help you with any other coding problems or provide more details about this solution?