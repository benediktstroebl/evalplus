```python
def fizz_buzz(n: int):
    count = 0
    for i in range(1, n+1):
        num = str(i)
        if num [0] == '7':  # Only check the first digit
            count += 1
    return count

# Test cases go here:
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(80) == 0
assert fizz_buzz(100) == 5
``` 
The above Python code defines a function `fizz_buzz` that counts the number of occurrences of the digit 7 in numbers less than a given number `n` that are divisible by 11 or 13. The function iterates throughs through numbers from 1 to `n` and checks if the first digit of the number is 7. It returns the count number of such occurrences of the digit 7 in such numbers.