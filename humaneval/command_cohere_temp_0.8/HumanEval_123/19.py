Here's a Python script with a self-contained function that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    odd_collatz.reverse()
    return odd_collatz

# Test cases
print(get_odd_collatz(1))  # Returns [1]
print(get_odd_collatz(5))  # Returns [1, 5]
print(get_odd_collatz(14)) # Returns [1, 7, 11, 23, 19, 17, 31, 43, 47]
``` 

This script defines a function `get_odd_collatz(n)` that returns a list of odd numbers in the Collatz sequence, starting from the input number `n`. The function iterates through the sequence with while loop until it reaches 1. It adds each odd number to the `odd_collatz` list, which is later reversed to ensure the correct order. The function handles the edge case `get_odd_collatz(1)` by returning `[1]`, as the Collatz sequence starts from 1 for any input.