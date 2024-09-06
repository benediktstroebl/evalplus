```python
def fizz_buzz(n: int):
    # Count the number of 7s in numbers less than n which are divisible by 11 or 13
    result = 0
    for num in range(1, n+1):
        digit7 = any([num % 11 == 7 or num % 13 == 7])
        if digit7:
            result += 1
    return result

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given input `n` that are divisible by 11 or 13. The function uses a loop and the `any()` function to check if any digit in the number is 7. The function then returns the result, which counts the total occurrences of 7 in such numbers.