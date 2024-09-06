```python
def smallest_change(arr):
    odd, even = 0, 0
    for i in range(len(arr)):
        if arr[i] % 2:
            odd += 1
        else:
            even += 1
    return min(odd, even)
```

The function examines each number in the array, classifying each as "odd" or "even" based on its modulo state by 2. It then calculates the count of each classification, comparing them to determine the minimum number of changes required, which is the task's solution.

This algorithm's efficiency is O(n), where 'n' is the array's size. It takes linear time to process each element once in a single pass. The algorithm is concise and directly solves the problem statement. It also avoids the complexity of sorting or explicit palindrome checks, making it both effective and readable.