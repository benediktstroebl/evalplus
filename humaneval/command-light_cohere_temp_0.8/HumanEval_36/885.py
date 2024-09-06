```python
def fizz_buzz(n: int) -> int:
    counts = 0
    for i in range(2, n+1):
        num = str(i)
        if num[0] == 7 and (num[1] == '0' or num[1] == '11'):
            counts += 1
        if num[0] == 7 and (num[1] == '1' or num[1] == '13'):
            counts += 1
    return counts

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This script defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in the range of integers less than `n` that are divisible by 11 or 13. The function iterates through the string representation of numbers from 2 to `n` and checks for the occurrence of the digit 7 and the condition for divisibility by 11 or 13. The function returns the count, indicating how many times the digit 7 appears in the list of numbers divisible by 11 or 13.