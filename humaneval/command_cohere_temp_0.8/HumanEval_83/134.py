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

This approach uses a straightforward accumulation approach. Beginning with the digits ranging from 1 to n, we count the numbers that end with 1. To accomplish this, we create a list called `counts` and initialize all its elements to 0. The numbers that end with 1 are then counted by iterating through the digits from 2 to n, incrementing the `counts` element for each number by the value of the element preceding it. Lastly, we return the value of `counts[n]`, which signifies the count of numbers ending in 1 and with n digits. 

The approach has a time complexity of O(n) and a space complexity of O(n) as well, making it an efficient solution.