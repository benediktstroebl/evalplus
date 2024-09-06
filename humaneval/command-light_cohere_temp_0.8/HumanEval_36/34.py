Here's the solution:

```python
def fizz_buzz(n: int) -> int:
    seen = set()
    
    for num in range(1, n+1):
        digit7 = int(num % 10)
        if digit7 in seen or num % 11 == 0 or num % 13 == 0:
            seen.add(digit7)
            
    return len(seen)
```

This function uses a set to count the number of occurrences of the digit 7 in numbers less than `n` which are either divisible by 11 or 13. The function then returns the process by iterating through the numbers from 1 to n, and adding the digit 7 to the set if the current number is divisible by 11 or 13.