```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr = a[i] + a[j]
            if curr % 3 == 0:
                triples += 1
    return triples
```

The script creates the array `a` as specified in the prompt, and then iterates through all possible pairs of elements in the array. If the sum of the two elements is divisible by 3, it adds 1 to the `triples` count. The function then returns the total count of triples. 

This solution achieves an efficient time complexity of `O(n^2)`, which is optimal for the given problem constraints. 

To test the function, you can call `get_max_triples()` with a specific value of `n` and compare the result with the expected output.