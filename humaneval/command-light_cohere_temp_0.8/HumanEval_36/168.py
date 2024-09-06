Here's the Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n: int):
    count = 0
    for num in range(2, n+1):
        if (10 * num) % 11 == 7 or (10 * num) % 13 == 7:
            count += 1
    return count
```

This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than `n` which are divisible by 11 or 13. The function iterates through through numbers from 2 to `n` and checks if the tens digit of each number is 7 or 13. The `count` variable is then incremented for each such number.