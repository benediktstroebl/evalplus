```python
def fizz_buzz(n: int):
    count = 0
    for num in range(2, n+1):
        if all(c % 11 or c % 13 for c in str(num)):
            count += 1
    return count

# Test cases
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```
This code defines a function fizz_buzz that calculates the number of times the digit 7 appears in the sequence of numbers from 2 to n, considering only divisibility by 11 or 13. The function iterates through a list of numbers from 2 to n, and checks if every number in this sequence has all its digits that are either odd (and therefore divisible by 13) or even (and therefore divisible by 11). The function counts the number of such satisfying numbers and returns the result.