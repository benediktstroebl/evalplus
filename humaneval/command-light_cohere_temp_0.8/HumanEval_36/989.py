Here's the solution:

```python
def fizz_buzz(n: int) -> int:
    seen = set()
    for num in range(1, n+1):
        digit = str(num)[0]
        if digit in seen or (digit == '7' and num % 11 == 0) or (digit == '8' and num % 13 == 0):
            seen.add(digit)
            continue
        return len(seen)
```

This function uses a set to keep track of the digits seen and iterates through numbers from 1 to n. It checks for each digit in the number to see if it has already been seen, if it's 7 or 8 and the number is divisible by 11 or 13, adds it to the set.