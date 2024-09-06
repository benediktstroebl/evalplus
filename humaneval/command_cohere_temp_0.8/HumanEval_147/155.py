```python
def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate maximum triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_ = a[i] + a[j] + a[j + 1]
            if sum_ % 3 == 0:
                max_triples += 1
    return max_triples
```
This script creates the sequence of numbers as described in the prompt and then iterates through all possible pairs of values (excluding the last value) and checks if the sum of the three values is a multiple of 3. This is done using the modulus operator '%' which returns the remainder of the division of the sum by 3. If the remainder is 0, meaning that the sum is divisible by 3, then it counts the occurrence as a triple that qualifies for the answer. The script then returns the maximum number of qualifying triples for the given sequence. 

This approach results in a time complexity of O(N^2) due to the nested for loop and a space complexity of O(N) to store the array. 
The approach can be enhanced using a more efficient algorithm inspired by the machinery principle which is used in the advanced solution.