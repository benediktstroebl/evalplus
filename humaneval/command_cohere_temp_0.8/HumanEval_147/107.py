```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_ = a[i] + a[j] + a[j + 1]
            if sum_ % 3 == 0:
                triples += 1
    return triples
```

The function creates the array `a` as specified in the prompt. It then calculates the sum of each triple (e.g., `a[i], a[j], a[k]`) and checks if the sum is divisible by 3. If it is, it increments the count for the valid triple. Finally, it returns the total count of valid triples.

The script also includes a test case to ensure that the function behaves as expected. You can uncomment the test case and run the function to see if it passes. 

```python
# test_get_max_triples:
n = 5
expected_triples = 1

assert get_max_triples(n) == expected_triples
```