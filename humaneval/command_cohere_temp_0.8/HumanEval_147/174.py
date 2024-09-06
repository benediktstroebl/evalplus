```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate sum of adjacent pairs to check triples
    pairs_sum = [arr[i] + arr[i-1] for i in range(1, n)]
    
    # Count multiples of 3
    triple_count = sum(1 for x in pairs_sum if x % 3 == 0)
    
    return triple_count
```

This script creates the array as prescribed in the question and then calculates the sum of adjacent pairs in the array. It then counts the occurrences of triples from the sums, which is achieved by iterating over the sums and checking if each sum is a multiple of 3, effectively counting the triples. This solution is efficient and easily scales with larger inputs.