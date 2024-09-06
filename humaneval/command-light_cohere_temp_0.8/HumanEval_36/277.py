Here's the code that implements the function `fizz_buzz`:

```python
def fizz_buzz(n: int) -> int:
    num_of_7 = 0
    for num in range(1, n+1):
        num = str(num)[1:]  # Convert integer to string
        if any(c == '7' for c in num):
            num_of_7 += 1
        if num % 11 == 0 or num % 13 == 0:
            break
    return num_of_7
```

This function uses a loop to iterate through numbers from 1 to `n`. It checks for each digit in the number, and counts how many of them are 7. If the number is divisible by 11 or 13, it's considered a valid number and the loop breaks early.

This function can be easily called and tested with different input values. The code is self-contained and doesn't rely on any other variables or functions.