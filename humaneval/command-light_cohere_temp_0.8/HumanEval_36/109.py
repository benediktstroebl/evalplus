Here's the solution to the problem:

```python
def fizz_buzz(n: int) -> int:
    count = 0
    for num in range(2, n+1):
        if all(c % 11 or c % 13 for c in str(num)):
            count += 1
    return count
```

This code defines a function fizz_buzz that calculates the number of occurrences of the digit 7 in numbers less than n and which are divisible by 11 or 13. It achieves this by iterating through numbers from 2 to n, and checking if all digits in the number's string representation are either odd or divisible by 11 or 13.