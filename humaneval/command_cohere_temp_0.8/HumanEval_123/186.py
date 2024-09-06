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
    odd_collatz.sort()
    return odd_collatz
```
This script defines a function `get_odd_collatz(n)` that returns a sorted list of odd numbers in the Collatz sequence for a given starting integer n. The function iterates through the Collatz sequence until it reaches 1, appending each odd number to the `odd_collatz` list. Finally, it sorts the list and returns the result.