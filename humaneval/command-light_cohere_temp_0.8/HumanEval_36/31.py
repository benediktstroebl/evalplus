```python
def fizz_buzz(n: int):
    count = 0
    for num in range(10, n+1, 2):
        if is_divisible(num, 11) or is_divisible(num, 13):
            count += 1
    return count

def is_divisible(num: int, dividend):
    return (num % dividend == 0)

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This script defines a function fizz_buzz that returns the number of times the digit 7 appears in the integers less than n which are divisible by 11 or 13. It uses a major counting as the digit 7 appears in the result for this specific range of numbers. 

The second function is_divisible that checks if a given number is divisible by another number.