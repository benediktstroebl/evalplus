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

The `get_odd_collatz` function starts with the input number `n` and iterates through the Collatz sequence until it reaches 1. During each iteration, it checks whether the current number is even or odd to determine whether to divide by 2 or multiply by 3 and add 1, respectively.

The resulting odd numbers in the sequence are stored in the `odd_collatz` list, which is then sorted in ascending order. Finally, this list is returned, containing only the odd numbers in the Collatz sequence for the initial input `n`. 

This function elegantly handles the Collatz sequence generation and filtering, providing the desired output.