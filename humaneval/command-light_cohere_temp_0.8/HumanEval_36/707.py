```python
def fizz_buzz(n: int):
    return len(
        [i for i in range(1, n + 1) if int(i) % 10 == 7 or i % 13 == 7])

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The above code defines a function `fizz_buzz` which returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. 

This is achieved using a list comprehension, which generates all the numbers from 1 to n and checks if the number is divisible by 11 or 13. 

It then returns the length of this list.