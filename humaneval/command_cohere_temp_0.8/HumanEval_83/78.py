```python
def starts_one_ends(n):
    # Create a list to store the results for 
    # different lengths of n
    counts = [0] * (n + 1)
    
    # For each length, determine the number of
    # numbers that start or end with 1
    for i in range(1, n + 1):
        counts[i] += 2 * 10 ** (n - i)
    
    return counts[n]
```
The function starts_one_ends() calculates the count of n-digit positive integers that start or end with 1. It uses a nested loop to iterate through all possible lengths of numbers from 1 to n and initially creates a list counts containing zeros, with each element representing the count for a specific length. Then for each length i, it calculates the count of numbers that start with 1 or end with 1, multiplying it by 2 to account for both possibilities and adding it to the appropriate count in the counts list. Finally, it returns the count of numbers that start or end with 1 for the given n. 

This approach has a time complexity of O(n^2), where n is the given number, which is the average time complexity for traversing matrixes, a matrix has been created with dimensions (n+1) x n.

The space complexity is also O(n), as we create a list of size n+1 and loop through it. We don't have any more significant operations that grow with the size of the number n, so the complexity remains linear. 

This problem can also be solved using the concept of annuities, but this solution is more intuitive and easier to grasp.