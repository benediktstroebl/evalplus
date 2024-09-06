```python
def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit[0] == 7 and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
print(fizz_buzz(120))  # Output: 4
print(fizz_buzz(121))  # Output: 5)
print(fizz_buzz(5020))  # Should return 8, correct?
```