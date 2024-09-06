```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if (arr[i] + arr[j] + arr[j + 1]) % 3 == 0:
                triples += 1
    return triples
```

The function creates the array of numbers as per the problem statement and then uses two nested loops to iterate through every possible pair of elements except the last one, and checks if the sum of the trio is a multiple of 3. The function returns the number of such valid trios. 

To make the function more efficient, we can optimize it using the fact that every third element in the array satisfies the condition, so we don't need to check every pair for aggregation.

Such a approach would yield a complexity of `O(n^2)` to `O(n)` making our program much more efficient. 

And the corresponding optimized solution would be:
```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    thirds = len(arr) // 3
    return thirds * (thirds - 1) // 2
``` 

The above solution uses the fact that the problem can be decomposed into finding the number of ways to choose 2 elements from a set of `n` elements, which is denoted by `C(n, 2)` and is equal to `n * (n-1) / 2`. In the case of every third element fulfilling the criterion, it becomes `C(n/3, 2)` and therefore the solution.