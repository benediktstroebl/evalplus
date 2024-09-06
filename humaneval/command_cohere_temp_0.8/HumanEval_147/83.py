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
This Python script defines a function `get_max_triples` that takes in a positive integer `n` as its input and creates an integer array `a` of length `n`, where each element in the array is defined as `i * i - i + 1`, for `i` ranging from 1 to `n`. The function then returns the number of triples (`a[i]`, `a[j]`, `a[k])` where `i < j < k`, and the sum of the elements in the triple (`a[i] + a[j] + a[k]`) is a multiple of 3. To compute the maximum number of such triples, the function iterates through all the possible pairs of indices `i` and `j`, checks if the sum of the corresponding array elements is divisible by 3, and increment the `max_triples` counter if it is. 

Here's an example of using this function with the input `n = 5`:
```python
get_max_triples(5)  # Output: 1
```
This should match the example's specified output and the function should correctly return 1 as the maximum number of triples that satisfy the given condition. 

I hope this solution aids you in your quest to solve the problem. Please let me know if you would like any additional adjustments to be made to the code or if you have any further questions.