```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_ = a[i] + a[j] + a[j + 1]
            if sum_ % 3 == 0:
                max_triples += 1
    return max_triples
```
This Python script defines a function `get_max_triples` that takes in a positive integer `n` as its input and creates an integer array `a` of length `n`, as per the problem statement. It then returns the number of triples (a[i], a[j], a[k]) of `a` where `i < j < k`, and `a[i] + a[j] + a[k]` is a multiple of 3.

The script returns the maximum number of qualifying triples for a size `n` array. It uses nested loops to iterate through all qualifying pairs of elements, calculates their sum, and checks if the sum is divisible by three. If so, it increments the count. Finally, the function returns the calculated number of triples. 
The code is self-contained and can be exported as is to be used in tests or problems that require solving this specific task. Hoped this helped! Let me know if you have any other questions.