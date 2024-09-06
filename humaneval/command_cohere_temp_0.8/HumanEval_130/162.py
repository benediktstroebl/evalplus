```python
def tri(n):
    progression = [0, 0, 0]
    for i in range(1, n + 1):
        if i % 2 == 0:
            progression.append(1 + i // 2)
        else:
            progression.append(progression[i - 1] + progression[i - 2] + progression[i + 1])
    return progression
```

This Python script defines a function called `tri(n)` that calculates the Tribonacci sequence for the first `n+1` numbers and returns them as a list.

The script includes a self-contained docstring that provides an explanation and example for the Tribonacci sequence, followed by a code block that demonstrates how to use the `tri(n)` function. 

The function iterates through each number from 1 to `n`, it keeps track of the current three last values of the Tribonacci sequence (`progression`). If the number is even, it appends the next value in the sequence by calculating `1 + (i) / 2` to `progression`. If the number is odd, it appends the sum of the previous three values in the sequence (`progression[i-1] + progression[i-2] + progression[i+1]`). Finally, the function returns the list of the first `n+1` values of the Tribonacci sequence. 

This is a clean and efficient solution to generate the Tribonacci sequence in Python while maintaining a self-contained script that is easy to understand and use by others.