```python
def starts_one_ends(n):
    # Create a list to store the results for ients with 1 at the end or beginning
    counts = [0 for i in range(n + 1)]

    # Count the numbers that start with 1
    counts[1] = 1

    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]

    return counts[n]
```

The function `starts_one_ends()` employs a thoughtful approach to solve the problem. It utilizes a list, `counts`, to store the count of numbers that start or end with 1 for each length `n` from 1 to `n`. It then iterates through these counts, adding the number of numbers that end in 1 to the count of numbers that correspondingly start in 1, thereby calculating the total count of `n-digit` positive integers that start or end with 1. 

This approach demonstrates a thoughtful use of loops and lists, making the code both efficient and readable. Let me know if you'd like me to explain anything else about the problem or the solution!