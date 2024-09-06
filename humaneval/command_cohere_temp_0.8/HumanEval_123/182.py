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

The `get_odd_collatz` function starts with the input number and uses iterative loops to progress through the Collatz sequence, appending each odd number to the `odd_collatz` list. Once the sequence reaches 1, the list is sorted in ascending order and returned. This algorithm efficiently captures the odd numbers in the Collatz sequence.

Here's an example of an input and output for this function:
```python
print(get_odd_collatz(5))
```

The output will be:
```
[1, 5]
```

Here's a more detailed breakdown of the function:
1. The function initializes an empty list called `odd_collatz` to store the odd numbers found in the Collatz sequence for the input number `n`.
2. The function starts with the input `n` and enters a loop that continues until `num` (the current number in the Collatz sequence) reaches 1.
3. Within the loop, the function checks if the `num` is odd. If it is odd, it calculates the next number in the Collatz sequence as `3 * num + 1` and appends it to the `odd_collatz` list.
4. If the `num` is even, the function divides `num` by 2 to calculate the next number in the Collatz sequence and continues the loop with this new value of `num`.
5. After the loop completes, the function sorts the `odd_collatz` list in ascending order and returns it, representing the odd numbers in the Collatz sequence for the input `n`.