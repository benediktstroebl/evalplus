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
This Python script defines a function called `get_max_triples` that takes in a positive integer n as its input. This function creates an integer array a with a length of n, where each element in the array is computed as i * i - i + 1 for all values of i from 1 to n. The purpose of this function is to calculate and return the number of unique triples (a[i], a[j], a[k]) within the array a, where i < j < k, and the sum of these three array elements is divisible by 3. The script demonstrates how the problem can be effectively solved by considering the conditions and iterating through the array elements.

Here's a breakdown of the code above:
1. The `get_max_triples` function is defined. It will be called with an integer argument n, and is expected to return an integer value.
2. The nested loop is used to iterate over the array elements `arr` of size `n`. The outer loop runs from index `i = 1 to n-1`, and the inner loop runs from index `j = i+1 to n-1`.
3. The variable `cnt` is used to keep track of the number of valid triples found.
4. Inside the nested loops, the condition `arr[i] + arr[j] + arr[j+1]) % 3 == 0` is used to check if the sum of the current three elements is divisible by 3. If the condition is satisfied, the `cnt` variable is incremented, marking the discovery of another valid triplet.
5. Once all combinations of `arr` within the size constraints are checked, the function returns the final value of `cnt`, which represents the maximum possible triples meeting the criteria in the array `arr`. 
This approach efficiently solves the problem by considering each element in the array and its relationships with other elements to satisfy the given condition.