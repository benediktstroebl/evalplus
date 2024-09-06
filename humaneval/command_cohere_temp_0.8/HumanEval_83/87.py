```python
def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit positive integer
    counts = [0] * (n * 9)
    
    # Iterate through potential starting digits from 1 to 9
    for start in range(1, 10):
        # Iterate through potential ending digits from 0 to n-1
        for end in range(0, n):
            # If the current potential number has a length of n
            if start + end + 1 == n:
                # Increment the count if the potential number starts or ends with 1
                if start == 1 or end == 0:
                    counts[end] += 1
    
    # Return the count of acceptable numbers
    return counts[-1]
```

The variable `counts` is a list that stores the count of numbers that start or end with 1 for each possible n-digit positive integer. This is an efficient approach that runs in constant time.

The two nested loops iterate through every possible starting digit (from 1 to 10-1) and every possible ending digit (from 0 to n-1). For each pair of starting and ending digits, the condition `start + end + 1 == n` checks if the current potential number has exactly n digits.

If the starting digit is 1 or the ending digit is 0, the count for the current potential number is incremented. The last element of the `counts` list (at index `n * 9 - 1`) is returned, which represents the count of numbers that start or end with 1 and have exactly `n` digits. 

This approach is computationally efficient and solves the problem by directly calculating the counts for each possible n-digit positive integer and returning the desired count.