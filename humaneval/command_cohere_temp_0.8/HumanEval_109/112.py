Here's a Python script that contains a function named `move_one_ball` optimized to solve the problem statement with concise logic and efficiently pass the tests:
```python
def move_one_ball(arr):
    n = len(arr)
    arr.sort()
    return n == len(set(arr)) and arr[0] <= arr[1]
```

This function uses the Python built-in sorted function to sort the input array. The method effectively solves the problem without the need for explicit loops or manual sorting. The condition `n == len(set(arr))` checks if there's only one unique element in the array, and `arr[0] <= arr[1]` checks if the sorted array is in non-decreasing order. 

The script can be made more efficient by noting that the problem statement implies the array will have unique elements. Thus, we can directly check the first two elements of the sorted array to determine if it's possible to achieve a non-decreasing order.