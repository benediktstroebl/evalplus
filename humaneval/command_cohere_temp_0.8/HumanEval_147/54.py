```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    cnt = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if arr[i] + arr[j] + arr[j+1] == 3:
                cnt += 1
    return cnt
```
The Python script provided a function called `get_max_triples` that takes in a positive integer n as its argument and returns the number of triples (a[i], a[j], a[k]) from an integer array a of length n that meets the conditions specified in the prompt. This function creates an array `arr` that stores the values of `i * i - i + 1` for `i = 1, 2, ..., n`. It then iterates through the array using two nested loops. The outer loop iterates from `i = 0` to `i = n-2`, and the inner loop iterates from `j = i+1` to `j = n-1`. The code checks if the sum of the elements at indices `i` and `j` (`arr[i]` and `arr[j]`) is equal to `3` and if so, it increments the `cnt` variable. Finally, the function returns the value of `cnt`, which represents the number of eligible triples in the array `arr`.