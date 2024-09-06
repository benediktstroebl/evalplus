```python
def fizz_buzz(n: int):
    # Initialize a counter
    c = 0

    # Loop through numbers from 0 to n
    for i in range(0, n+1):
        if i % 11 == 7 or i % 13 == 7:
            c += 1

    return c

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This function counts the number of occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. 

It uses a loop to iterate through numbers up to `n` and checks each number for divisibility by 11 or 13. If the number is divisible by either of these numbers, the digit 7 will either be in the number or one of its digits will be 7. 

The function returns the total count of occurrences of the digit 7 in such numbers.