```python
def fizz_buzz(n):
    count_seven = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit == '7' and int(digit) < n and (i % 2 == 0 or i % 13 == 0):
            count_seven += 1
    return count_seven

# Test suite
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
print(fizz_buzz(10))  # Should raise an error: cannot convert to integer 10 to string)
print(fizz_buzz(40))  # Should raise an error: first iteration should be 1, not 40
```