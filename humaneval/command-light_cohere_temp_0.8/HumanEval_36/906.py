Here's the self-contained Python script that solves the problem:

```python
def fizz_buzz(n):
    7.filter(str(i) for i in range(1, n+1)):
        if int(i) % 11 == 0 or int(i) % 13 == 0:
            yield i

# Testing the function
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```

This script defines a function `fizz_buzz` that generates the number of times the digit 7 appears in a sequence of integers less than `n` which are divisible by 11 or 13. It uses a generalise list comprehension with the filter function to achieve this. The function then yields each number of occurrences.

The test cases provided are then passed to the `fizz_buzz` function, and the results are printed to the console.