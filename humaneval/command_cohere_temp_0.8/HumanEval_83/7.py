Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the markdown code block:
```python
def starts_one_ends(n):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Different ways to arrange 1 followed by n-1 digits
    counts[0] = 1  # There's one way to have 1 followed by 0-1 digits, and that is simply "1" itself.

    for i in range(1, n):
        prev_dig = 1
        curr_dig = 1
        for j in range(i - 1, 0, -1):
            if j == 0:
                counts[i] += prev_dig * curr_dig
            else:
                counts[i] += prev_dig * (10 - j) // (j + 1)
                counts[i] += curr_dig * (j - 1) // (j + 1)
            prev_dig = 10 // (j + 1)
            curr_dig = (10 - j) // (j + 1)
        prev_dig = 1
        curr_dig = 1
        for j in range(i + 1, n + 1):
            if j == n:
                counts[i] += prev_dig * curr_dig
            else:
                counts[i] += prev_dig * (10 - j) // (j + 1)
                counts[i] += curr_dig * (j - 1) // (j + 1)
            prev_dig = 10 // (j + 1)
            curr_dig = (10 - j) // (j + 1)
    return sums[n]
```
This approach employs dynamic programming to efficiently compute the count of positive integers that start or end with 1 within a given range. It uses a nested loop to iterate through each possible length of the positive integer, considering both starting and ending 1 configurations, and accumulates the counts accordingly. The base case of the nested loop, where one of the digits is 0, ensures an accurate count for each particular length. The result is the sum of counts for all relevant lengths.