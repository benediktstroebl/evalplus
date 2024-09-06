```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    cnt = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if (arr[i] + arr[j] + arr[j+1]) % 3 == 0:
                cnt += 1
    return cnt
```
The solution is a brute force approach, where we first create the array of values for all elements from 1 to n, and then iterate through all pairs of elements and check if the third element (whose value is known) makes the sum divisible by 3.