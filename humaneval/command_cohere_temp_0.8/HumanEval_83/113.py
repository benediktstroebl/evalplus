```python
def starts_one_ends(n):
    # Create a list to store the results for bases from 1 to n
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[n]
```

This approach uses the concept of counting numbers in different bases. The function counts the numbers that start with 1 (having base 1) and counts the numbers that end with 1 (having base n) and then sums these counts properly.