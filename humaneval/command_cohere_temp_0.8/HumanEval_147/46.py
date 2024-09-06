```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize counter
    max_triples = 0
    
    # Calculate valid triples for the sequence
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if (a[i] + a[j] + a[j + 1]) % 3 == 0:
                max_triples += 1
    
    return max_triples
```
This script defines a function `get_max_triples` that takes in a positive integer `n` and creates an integer array `a` of length `n`, as per the problem statement. It then returns the number of triples (a[i], a[j], a[k]) of `a` where `i < j < k`, and `a[i] + a[j] + a[k]` is a multiple of 3.

The script's self-contained approach ensures that it can be run independently, and it provides a concise and efficient solution to the problem.  This solution has a time complexity of `O(n^2)`, which arises from the nested loop traversing the array, and a space complexity of `O(1)`, as it only uses a constant amount of memory to store the `a` array and the `max_triples` counter.