```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if (arr[i] + arr[j] + arr[j + 1]) % 3 == 0:
                cnt += 1
    return cnt
```
This Python script defines a function called `get_max_triples` that takes in a positive integer `n` as its input and returns the number of triples from the array `arr` where `i < j < k` and `a[i] + a[j] + a[k]` is a multiple of 3. The function creates an array `arr` of length `n` with each element computed as `i * i - i + 1` for all `i`. It then iterates through the array and counts valid triples. 

The time complexity of the program is O(N^2) due to the nested loop structure.