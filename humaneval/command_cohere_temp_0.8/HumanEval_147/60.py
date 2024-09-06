```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples
    curr = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_ = a[i] + a[j] + a[j + 1]
            if sum_ % 3 == 0:
                curr += 1
    return curr
```

The script uses nested loops to iterate through all valid triples (where the sum is divisible by 3) of adjacent elements in the sequence `a` that it defines. It then counts the valid triples and returns the number of them, which is the answer to the problem. 

This approach ensures that the code is self-contained and does not rely on any external variables or functions. 

The `a` list is a linear sequence whose elements are derived from the formula `i * i - i + 1` for `i = 1 to n`. Such a sequence is commonly used in mathematical problems related to arrays and matrices, and understanding the intrinsic mathematical nature of the sequence helps solve the problem efficiently. 

The code solves the specified problem while maintaining a self-contained Python script that can be executed independently to pass the test case.