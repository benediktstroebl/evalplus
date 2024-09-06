```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    triple_count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if (a[i] + a[j] + a[j + 1]) % 3 == 0:
                triple_count += 1
    return triple_count
```

The script employs nested loops to iterate through all possible pairs of elements and checks if the sum of the three elements in the array forming a triangle (including the current element and the next element) is divisible by 3. The maximum number of triangles is then returned by the program.

To ensure that the produced solutions are accurate, ample testing is required, including edge cases. In this exercise, only the length of the array is being varied to verify various scenarios. The test case for `n = 5` in this problem statement returns 1, which is the correct solution.