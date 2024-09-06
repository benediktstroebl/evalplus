```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples where a[i] + a[j] + a[k] is a multiple of 3
    # By observing patterns in the array, we can determine there will always be a multiple of 3 at indices n, n//2, and 0
    # So the number of triples will be the maximum of the three elements surrounded by these indices
    return max(arr[0], arr[n//2], arr[n])
```