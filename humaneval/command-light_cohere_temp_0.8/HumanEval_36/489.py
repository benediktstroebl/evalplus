```python
def fizz_buzz(n):
    total_times_7 = 0
    for i in range(1, n+1):
        num = str(i)
        if num [7] == '7':
            total_times_7 += 1
        num = int(num)
        if num % 11 == 0 or num % 13 == 0:
            pass
        else:
            continue
    return total_times_7

# Test suite
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```
The fizz_buzz function counts the number of times the digit 7 appears in the numbers less than n and then returns the result. This code is using a simple and clear approach to the problem.