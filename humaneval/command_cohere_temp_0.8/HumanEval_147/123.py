```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate maximum triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            current_sum = a[i] + a[j]
            max_triples = max(max_triples, len(list(filter(lambda x: x == current_sum, [a[k] for k in range(n) ]))))
    return max_triples
```
This script creates the sequence a as per the prompt, and then iterates through all possible pairs of indices i and j, where i is the smaller index and j is the larger index. It then calculates the sum of a[i] and a[j] and counts the number of values in the array a that result in this sum being a multiple of 3. This count is then added to the max_triples variable, which is returned at the end of the function.

Here is a breakdown of the script:
- The self-contained function `get_max_triples(n)` takes an integer n as input, where n is the length of the array a.
- It creates the array a of length n, where each element is calculated as i * i - i + 1. 
- The variable max_triples is initialized to 0.
- The nested loops i and j iterate through all pairs of elements in a. The loop variables i and j assume the role of the smaller and larger indices, respectively. 
- Within the nested loops, the sum of a[i] and a[j] is calculated.
- The length of the filtered list of values from a that have the current_sum is calculated using the filter function and the lambda expression. This list is where the triple should be (a[i], a[j], a[k]), so the length of this list is the number of possible values of a[k] that would make the sum a multiple of 3. This value is assigned to max_triples, which is now the maximum number of triples for the current i and j.
- The max_triples variable is returned at the end of the function. 

Note that this script assumes that the input n is a positive integer and that the provided time and space complexities are approximate.