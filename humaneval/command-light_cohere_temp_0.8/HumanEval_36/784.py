```python
def fizz_buzz(n: int) -> int:
    if n <= 0:
        return 0
    
    # Count the occurrences of 7 in numbers less than n
    count = sum(1 for num in range(10, n + 1, 9) if num % 10 == 7)
    
    # Count the numbers less than n that are divisible by 11 or 13
    result = count + (count == 1)
    
    return result
```