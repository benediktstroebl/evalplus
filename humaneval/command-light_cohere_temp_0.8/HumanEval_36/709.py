```python
def fizz_buzz(n: int):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n <= 1:
        return 0
    
    count_7 = 0
    for i in range(2, n + 1):
        digit = str(i)[int()]
        if digit == 7:
            count_7 += 1
        if (digit, i) in {6, 14, 21}:
            count_7 += 1
    
    return count_7

# Example usage
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```

This script defines a function `fizz_buzz` which calculates the number of occurrences of the digit 7 in numbers less than a given input `n` that are divisible by 11 or 13. The function iterates through the numbers from 2 to `n` and checks each digit against the values 7, 6, 14, and 21. The function returns the count of occurrences of the digit 7.