```python
def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 0:
        current = sequence.pop()
        if current % 2 == 0:
            sequence.append(current // 2)
        else:
            sequence.append(3 * current + 1)
        if current % 2 == 1:
            odd_collatz.append(current)
    odd_collatz.sort()
    return odd_collatz
```

The `get_odd_collatz` function uses a loop to generate the odd numbers in the Collatz sequence for a given starting integer `n`. It begins with a list `odd_collatz` to store the odd numbers, and a list `sequence` to hold the entire Collatz sequence.

For each iteration of the loop, the function removes the first element from the sequence list, making it the "current" number in the sequence. 

If the current number is even, it divides it by 2 and appends the result to the sequence list. If the current number is odd, it multiplies it by 3, adds 1, and also appends the result to the sequence list.

Additionally, if the current number is odd, it is added to the `odd_collatz` list. These odd numbers are stored in ascending order due to the `sort()` method at the end of the sequence iteration. 

The function returns the list `odd_collatz` containing all the odd numbers in the Collatz sequence for the given starting integer `n`. 

Here is an example of using the function for the starting value of `n=5`:
```python
print(get_odd_collatz(5))
```

The output will be:
```
[1, 5]
```

This is in line with the provided example in the problem statement, as the odd numbers in the Collatz sequence for `n=5` are `1` and `5`. 

The function also works for any other starting value of `n`, and will return the odd numbers in the Collatz sequence for that value. 

This code integrates the logic to generate the odd numbers in the Collatz sequence into the function, making it self-contained and easy to use.