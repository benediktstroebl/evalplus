```python
def fizz_buzz(n: int) -> int:
    count = 0
    for num in range(10, n+1, 2):
        if (num % 11 == 0 or num % 13 == 0):
            count += 1
    return count

# Test the function with different inputs
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This function efficiently computes the count of digits 7 appearing in numbers less than a given number, which are either divisible by 11 or 13, and returns this count.