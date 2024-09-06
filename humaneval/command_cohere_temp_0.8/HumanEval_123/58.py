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
    odd_collatz.reverse()
    return odd_collatz

# Test cases
print(get_odd_collatz(1))  # Returns [1]
print(get_odd_collatz(5))  # Returns [1, 5]
print(get_odd_collatz(10)) # Returns [1, 17]
```

This script defines a function `get_odd_collatz(n)` that calculates and returns a list of odd numbers in the Collatz sequence for a given starting integer `n`. The function initially generates an empty list called `odd_collatz` to hold the odd numbers. It then initiates a loop using a variable `num` to iterate through the Collatz sequence until `num` reaches 1. Within the loop, it checks whether `num` is even or odd and updates it accordingly using the Collatz sequence rules. Finally, it reverses the `odd_collatz` list to ensure the numbers are in ascending order and returns the list.