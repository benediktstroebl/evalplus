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

The solution leverages nested loops to iterate through all valid triples and calculates the sum of the three values in the triple. If the sum is divisible by three, it adds a valid triple to the count. To ensure that only distinct values are counted, the first value of the triple is assumed to be `a[i]`, the second value is assumed to be `a[j]`, and the third value is assumed to be `a[j + 1]`.

The code has a time complexity of O(n^2) due to the nested loops and a space complexity of O(1) as it only uses a constant amount of extra space to store the `a` list. 

The code includes a unit test that checks the correctness of the function by providing a specific input and comparing the output to the expected result. You can use it by calling:
```python
# Call the function with specific input
n = 5
expected_output = 1
actual_output = get_max_triples(n)

# Compare the actual output with the expected output
assert actual_output == expected_output
``` 
The given example will return the expected result of 1, as explained in the problem statement.