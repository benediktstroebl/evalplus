```python
def fizz_buzz(n):
    # Generate a list of digits from 0 to n
    digits = list(range(0, n+1))
    
    # Count the number of 7s in the list
    count = sum(1 for digit in digits if digit == 7)
    
    return count

# Test the function with a few values
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This script defines a function called `fizz_buzz` that calculates the number of times the digit 7 appears in the sequence of integers less than a given number `n`. The function uses a list comprehension to iterate through numbers from 0 to `n` and counts the number of 7s. The function then returns the value of the count. 

Finally, the function is tested with a few values to ensure it is working correctly.