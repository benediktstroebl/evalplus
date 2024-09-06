```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    m = 0
    for i in range(1, n+1):
        digit = ord('7')
        count = 0
        while True:
            d = str(i % 10)
            if d == '7':
                count += 1
            elif d == '11':
                break
            elif d == '13':
                count += 1
            else:
                break
        m += count
    return m

# Test the function
for i in range(50,78):
    print(fizz_buzz(i), end='\n')
```