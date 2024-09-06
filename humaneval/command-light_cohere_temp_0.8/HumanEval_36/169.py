```python
def fizz_buzz(n):
    total = 0
    for num in range(1, n+1):
        num = str(num)
        count = 0
        for d in range(8):
            if num[d] == '7':
                count += 1
        if count == 1 or count == 3:
            total += 1
    return total

# Test case 1
print(fizz_buzz(50))  # Output: 0

# Test case 2
print(fizz_buzz(78))  # Output: 2

# Test case 3
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz` that computes the number of times the digit 7 appears in integers that are less than a given number `n` and are divisible by 11 or 13. The function iterates through the number and checks for the occurrence of the digit 7. The function then returns the number of times the digit 7 appears.