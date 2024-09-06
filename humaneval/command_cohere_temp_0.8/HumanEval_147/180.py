```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples result
    max_triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = a[i] + a[j]
            if current_sum % 3 == 0:
                max_triples += 1
    
    return max_triples
```

This script creates the array `a` as described in the prompt, and then iterates through all possible pairs of elements in the array. If the sum of the two elements is divisible by 3, it indicates a valid triple that satisfies the problem's condition, and the maximum number of these valid triples is counted and returned. 

The `max_triples` variable is initialized to zero and incrementally populated as the nested loops iterate through all possible pairs of elements in the array, ensuring that the solution is correctly computed.