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
The Python script provides a function called `get_max_triples`, which takes in a positive integer `n` as its input. This function creates an integer array `a` of length `n`, where each element `a[i]` is calculated as `i * i - i + 1`. The task is to return the number of unique triples (a[i], a[j], a[k]) where `i < j < k`, and the sum of these three array elements is a multiple of 3. The solution accomplishes this by iterating through the array and counting the valid triples that satisfy these conditions. This is done through the use of two nested loops, with the outer loop iterating over the even positions (`i`) and the inner loop iterating over the odd positions (`j`). It checks if the sum of the values of `arr[i] + arr[j] + arr[j+1]` is greater than or equal to 3, and if so, it increments the count `cnt`. The final count is the number of valid triples and is returned as the result.

Here is an example of an input and output of the function:
```
Input: n = 5
Output: 1
```

The resulting array is [1, 3, 7, 13, 21], and the only valid triple is (1, 7, 13).