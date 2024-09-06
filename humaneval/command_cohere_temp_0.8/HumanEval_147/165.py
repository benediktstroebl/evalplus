```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    # triples that sum up to a multiple of 3
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            total = arr[i] + arr[j] + arr[j + 1]
            if total % 3 == 0:
                triples += 1
    return triples
```
The solution is a direct programming approach to generate the array and iterate over all possible pairs of elements and check if the third element satisfies the condition.

This solution has a time complexity of O(N^2) and is efficient enough to pass the majority of test cases. However, for very large inputs, a more optimized approach might be preferable. 

Feel free to ask if you'd like to discuss further or explore other possible approaches!