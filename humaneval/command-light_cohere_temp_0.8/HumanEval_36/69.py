Here's the code you asked for:
```python
def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(1, n+1):
        digit = str(i)[0]
        if digit == '7':
            count += 1
        num = int(str(i)[1:])
        if num % 11 == 0 or num % 13 == 0:
            pass
        else:
            count += 3
    
    return count
```

This script defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in the sequence of numbers less than `n` and which are divisible by 11 or 13. The function utilizes a loop to iterate through the numbers and counts the occurrences of the digit '7'. It then returns the total count of such digits.