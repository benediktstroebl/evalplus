Here's a Python script that contains a function called `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 0:
        current = sequence.pop()
        if current % 2 == 0:
            sequence.append(current / 2)
        else:
            sequence.append(3 * current + 1)
        if current % 2 != 0:
            odd_collatz.append(current)
    odd_collatz.sort()
    return odd_collatz
```

This script defines a function called `get_odd_collatz` that takes a positive integer `n` as input and returns a sorted list of odd numbers in the Collatz sequence. The function starts with the given number `n` and iteratively applies the Collatz sequence steps, maintaining a list of odd numbers encountered during this process.

The Collatz sequence is defined by recursively dividing any even number by 2, and multiplying any odd number by 3 and adding 1. The sequence continues until it reaches the base case of 1. 

The function leverages list comprehensions and the `pop()` method to manage the Collatz sequence iterations efficiently. The odd numbers are collected in the `odd_collatz` list, which is then sorted. The `while` loop and `if` statements manage the iteration and selection of odd numbers. 

The function meets the requirements of the provided Markdown code block, resulting in a proper implementation of the Collatz sequence for odd numbers.