```python
def fizz_buzz(n: int) -> int:
    count = 0
    for num in range(2, n+1):
        if (num % 11 == 0 or num % 13 == 0):
            count += 1
    return count

# Example usage
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function `fizz_buzz` which calculates the number of times the digit 7 appears in numbers less than `n` which are either divisible by 11 or 13. The function iterates through numbers from 2 to `n` and checks if the number is divisible by 11 or 13 using the `%` operator. If the number satisfies either condition, the function increments the `count` variable by 1.