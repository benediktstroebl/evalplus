```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize variables to track unique triples and multiples of 3
    triples = 0
    multiple_of_3 = 0
    
    # Loop through all combinations of size 3
    for i in range(n-2):
        for j in range(i+1, n):
            current_sum = a[i] + a[j] + a[j+1]
            if current_sum % 3 == 0:
                triples += 1
                multiple_of_3 += 1
    
    return triples // 3
```

This Python script defines a function `get_max_triples` that takes in a positive integer `n` as its input and creates an integer array `a` of length `n`, as mandated by the problem statement. The function then calculates the number of triples (`a[i], a[j], a[k])` where `i < j < k` and the sum of the values in each triple is a multiple of 3.

The solution utilizes a nested loop to iterate through all possible pairs of indices `i` and `j` (with `i` being the smaller index) and calculates the sum of `a[i]` and `a[j]` and the potential third value for the triple. If the sum is a multiple of 3, both the `triples` and `multiple_of_3` variables are incremented. The solution ultimately returns the maximum number of triples divided by 3, as the answer is given as the number of multiples of 3 in the `a` array.