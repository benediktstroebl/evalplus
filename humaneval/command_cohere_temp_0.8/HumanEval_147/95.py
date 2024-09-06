```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate occurrences 3 in arr[i] + arr[j] + arr[k]
    occur = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    occur += 1
    
    return occur
```

The solution is based on generating the array `arr` as specified in the prompt. We then iterate over all possible triples (`arr[i]`, `arr[j]`, `arr[k])`, and count the occurrences where `arr[i] + arr[j] + arr[k]` is divisible by 3. This gives the final count of valid triples.

This approach results in an time complexity of `O(n^3)` due to the explicit triple-loop traversal. There are more efficient approaches possible, especially if you can leverage existing knowledge about the `arr` generation or employ some sorting/batching. However, the provided solution follows the direct specification and gives a correct output.