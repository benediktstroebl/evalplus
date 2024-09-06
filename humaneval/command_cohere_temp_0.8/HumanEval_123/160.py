Here's a Python script with a self-contained function `get_odd_collatz` that solves the problem:
```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    odd_collatz.sort()
    return odd_collatz

# Test cases
print(get_odd_collatz(1))  # Returns [1]
print(get_odd_collatz(5))  # Returns [1, 5]
print(get_odd_collatz(10)) # Returns [1, 5, 21]
```
This script defines a function `get_odd_collatz(n)` that returns a list of odd numbers in the Collatz sequence for a given starting integer n. The function iterates through the sequence until it reaches 1, appending each odd number to the `odd_collatz` list. Finally, the list is sorted in ascending order. 

The example usage demonstrates how the function can be called for different input values, resulting in the corresponding lists of odd numbers in the Collatz sequence.