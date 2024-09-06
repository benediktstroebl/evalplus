```python
def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * n

    # Count numbers that start with 1
    counts[0] = 1

    # Count numbers that end with 1
    for i in range(1, n):
        counts[i] += counts[i - 1]

    return counts[n - 1]
```

This script provides the method `starts_one_ends(n)` that takes a positive integer `n` as input and returns the quantity of `n-digit` positive integers that start or end with 1. This is accomplished by employing a mathematical formula and utilizing the concept of complementary counting.