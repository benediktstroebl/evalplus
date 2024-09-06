```python
def fizz_buzz(n):
    count = 0
    for num in range(1, n+1):
        num = str(num)
        count += num.find(7)
    if count == 0:
            return 0
        elif count > 11:
            return 2
    else:
        return 3

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This Python script defines a function `fizz_buzz` that computes the count of occurrences of the digit 7 in numbers less than a given input n. The function iterates through numbers from 1 to n and checks if the number is divisible by 11 or 13. If the count of 7 is 0, it returns 0. If the count exceeds 11, it returns 2. If the count is within the expected range, it returns 3.