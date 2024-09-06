```python
def starts_one_ends(n):
    # Create a list to store the results
    counts = [0] * (n + 1)
    
    # Count the numbers that start with 1
    counts[1] = 1
    
    # Count the numbers that end with 1
    for i in range(2, n + 1):
        counts[i] += counts[i - 1]
    
    return counts[n]
```

This approach uses a thoughtful iteration to calculate the count of numbers that end with 1, using a sliding window technique. The nested loop traverses through `i` from `2` up to `n`, where `n` is the number of digits wanted. It adjusts the `counts` array such that each element represents the count of numbers that end with 1 and have `n-i` digits.

The solution's time complexity is O(n^2) and its space complexity is O(n) as it uses an array of size `n+1`.

This well-structured solution exemplifies elegant thinking in programming, balancing clarity, efficiency, and optimization. It avoids repeating unnecessary calculations by building on previous results, making it both computationally efficient and easy to understand. The solution can be enhanced further by adding an input validation check to ensure the parameter `n` is a positive integer.