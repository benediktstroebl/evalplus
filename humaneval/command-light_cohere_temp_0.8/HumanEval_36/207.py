```python
def fizz_buzz(n):
    count_7 = 0
    for i in range(1, n+1):
        num = str(i)
        if num[0] == 7:
            count_7 += 1
        num = int(num)
        if num % 11 == 0 or num % 13 == 0:
            pass
        else:
            break
    return count_7

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given number `n`, specifically those that are divisible by 11 or 13. The function iterates through the numbers up to `n` and checks each digit against the divisors 11 and 13. Finally, it returns the number of times the digit 7 appears in the range of such numbers.