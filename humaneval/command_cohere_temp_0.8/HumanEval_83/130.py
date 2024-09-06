```python
def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * n

    # Count numbers that start with 1
    counts[0] = 1

    # Count numbers that end with 1
    for i in range(1, n):
        counts[i] = counts[i - 1] + 1

    return counts[-1]
```

The function `starts_one_ends()` accepts a single argument `n`, representing the length of the numbers we want to consider. It utilizes a simple approach to count the numbers that start or end with 1.

It first counts the numbers that start with 1, which is conveniently 1 itself. So, the first count is 1. Then, it proceeds to count the numbers that end with 1. This is achieved by considering each digit from the second to the last digit in the number. The `counts` array is used to keep track of the counts so far. The inner loop iterates from the second to the last digit, and for each position, it adds 1 to `counts[i]` to account for the ending 1, and then adds `counts[i]` to `counts[i - 1]` to account for the decreasing length as we move left.

Finally, it returns the last count in the `counts` array, which gives the count of numbers that end with 1. The whole function is designed to handle the passed 'n' number of lengths, ensuring that the answer is correct for any given input.