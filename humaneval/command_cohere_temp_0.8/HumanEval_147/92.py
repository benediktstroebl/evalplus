```python
def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n + 1)]
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] + arr[j + 1]) % 3 == 0:
                cnt += 1
    return cnt
```
This Python script defines a function called `get_max_triples` that takes in a positive integer n as its input. This function creates an integer array a with a length of n, where each element in the array is computed as i * i - i + 1 for all values of i from 1 to n. The goal is to determine the number of unique triples (a[i], a[j], a[k]) where i < j < k, and the sum of these three array elements is divisible by 3. The function achieves this by iterating through the array and checking if the adjacent elements satisfy the condition where their sum is divisible by 3. The total number of such qualifying triples is counted and returned as the result.

The logic of the code is encapsulated within the function, and the implementation is self-contained without relying on external variables or defined elsewhere. This adheres to the problem statement's requirement for a self-contained solution.