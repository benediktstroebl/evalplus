Here's the solution to the problem:
```python
def fizz_buzz(n: int) -> int:
    total = 0
    for num in range(2, n + 1):
        count = 0
        for i in range(10):
            if num % i == 0 and i != 7:
                count += 1
        if count > 0:
            total += count
    return total
```

This function fizz_buzz is designed to calculate the number of times the digit 7 appears in the sequence of numbers less than `n` which are divisible by 11 or 13. It iterates through through through the start from the number 2 and loop up to the number n. It then uses another loop to iterate through the digits from 0 to 9. It checks if the count of each digit is greater than 0. If so, it adds the count to the total variable.

Finally, the function returns the value of total.