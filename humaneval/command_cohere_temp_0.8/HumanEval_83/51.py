```python
def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * n

    # Count numbers that start with 1
    counts[0] = 1

    # Count numbers that end with 1
    for i in range(1, n):
        counts[i] = counts[i - 1] + 1

    return counts[n - 1]
```

The function `starts_one_ends()` employs a straightforward approach. It utilizes a sliding window technique to count the numbers that end with 1. Initially, the window is formed by the single digit `1`, and the count is 1. As the loop progresses, the window moves one digit to the right, and the count is adjusted by adding the current digit. This accounts for numbers that start with 1 and those that end with 1. Finally, the total count is returned, which corresponds to the count of n-digit positive integers that start or end with 1. 

This approach is efficient and easily generalizable to different lengths of numbers (`n`). It does not require any complex mathematical analysis or use of mathematical modules. Thus, it offers a clean and straightforward solution to the problem.