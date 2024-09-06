```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate maximum triples
    curr = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            curr = max(curr, (a[i] + a[j] + a[j + 1]) // 3)
    return curr
```

The problem can be solved by generating the array `a` as required in the prompt. The maximum number of triples that satisfy the condition can then be computed by iterating over all possible pairs of elements in the array and maximizing the expression `a[i] + a[j] + a[k]` for all valid triples. The above code does exactly that, where `curr` is used to keep track of the maximum number of qualifying triples. The self-contained function should be able to run independently and return the correct output for the given `n` without any external dependencies.  This solution has a time complexity of `O(n^2)` since it requires two nested loops to iterate over all qualifying triples.  It should be noted, however, that this approach has a peak memory usage of `O(1)` since it is a simple iterative algorithm and thus does not require additional memory provisioning for each loop iteration.