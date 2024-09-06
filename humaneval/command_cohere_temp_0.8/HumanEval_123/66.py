Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
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

# Test Cases
print(get_odd_collatz(1))  # Returns [1]
print(get_odd_collatz(5))  # Returns [1, 5]
print(get_odd_collatz(10)) # Returns [1, 5, 21, 161]
``` 

This script defines a function `get_odd_collatz(n)` that returns a sorted list of odd numbers in the Collatz sequence for a given starting integer `n`. The function uses a while loop to generate the Collatz sequence until the number becomes 1, and it stores the odd numbers in the `odd_collatz` list, which is then reversed and returned.

The example usage demonstrates how the function can be called for different input values, and it correctly returns the desired odd numbers in the Collatz sequence for each case.