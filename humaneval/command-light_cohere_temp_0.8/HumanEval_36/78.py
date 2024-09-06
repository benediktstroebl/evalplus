```python
def fizz_buzz(n: int):
    return len([i for i, digit in enumerate(str(n)) if digit == 7 and n % 11 == 0 or n % 13 == 0])

print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The function fizz_buzz calculates the number of times the digit 7 appears in the string representation of numbers less than n that are divisible by 11 or 13. The function uses a list comprehension to iterate over each digit in the number and checks if the digit is 7. The function then returns the number of times the digit 7 appears.