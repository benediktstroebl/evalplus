Here's the solution:

```python
def fizz_buzz(n):
    if n <= 0:
        return 0
    s = set()
    for i in range(2, n+1):
        digit = str(i)[0]
        if digit == '7':
            s.add(i)
    if i % 11 == 0 or i % 13 == 0:
            s.add(i)
    count = s.count(digit)
    if count > 0:
        return count
```

This function uses a set to store the numbers that contain the digit 7. It iterates through loop from 2 to n, checking each number for the presence of 7 and incrementing the counter if the digit is found.