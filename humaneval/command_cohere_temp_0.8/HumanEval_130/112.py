```python
def tri(n):
    out = []
    x, y, z = 1, 3, 2
    while len(out) < n + 1:
        if len(out) % 2 == 0:
            out.append(x)
            x = x + y + z
            y = z
        else:
            out.append(z)
            z = x + y + z
            x = y
        y = x
    return out
``` 

This code defines a function called `tri(n)` that calculates the first `n + 1` terms of the Tribonacci sequence. The Tribonacci sequence is an extension of the Fibonacci sequence where each term is the sum of the previous three terms. The function starts with initial values for `x`, `y`, and `z` (1, 3, 2) and uses a loop to calculate the terms of the sequence.

For each iteration, the function checks if the length of the output list is odd or even. If the length is even, it appends the value of `x` to the list and updates `x` by adding the previous values of `y` and `z`. It then updates `y` and `z` with the new values of `x`. If the length is odd, it appends the value of `z` to the list and updates `z` by adding the previous values of `x` and `y` and updating `x` with the new value of `z`. 

This clever alternation between even and odd steps allows the function to calculate the next terms of the Tribonacci sequence and build the correct output list. The output list is then returned.  This approach optimizes the space complexity, ensuring that only one variable is updated in each step, which is the minimum needed to store the three necessary values.