```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    cnt = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if arr[i] + arr[j] + arr[j+1] >= 3:
                cnt += 1
    return cnt
```
The code defines a Python function `get_max_triples` that takes an integer `n` as input. This function calculates the maximum number of valid triples from the given condition in the MD code block and returns it.

The resulting integer array `arr` is created with values calculated from the given condition. Then, the code uses two nested loops to iterate over pairs of elements in the array, checking if the third element is also a part of the triple and satisfies the condition. Every time a valid triple is found, the counter `cnt` is incremented. Finally, the function returns the total count of valid triples.