```python
def can_arrange(arr):
    prev = arr[0]
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            idx = i + 1
            break
    return max(idx, -1)
```

The function iterates through the array, comparing each element to the previous one. If they are not in order, a possible answer is the current index, which is tracked by the `idx` variable. If the current element is not greater than or equal to the previous one, the loop continues. If a point is reached where the criterion is met, the index of that element is returned, or -1 if the entire array is in order. The maximum between this index and -1 is then returned as the final answer. 

This approach is efficient as it has a time complexity of O(n) and a space complexity of O(1), which is optimal for this problem. Additionally, the function is scalable and can handle arrays of various sizes and elements. 

To better understand how the function works, here is a breakdown of the code:
1. The function `can_arrange` takes an array `arr` as input.
2. The first element of the array is assigned to the variable `prev` and the index is set to 0.
3. The loop iterates through the array starting from the second element to the last element.
4. For each iteration, the current element is compared to the previous element using the condition `arr[i] >= arr[i - 1]`.
5. If the condition is true, it means that the current element is not greater than or equal to the previous element, and the index is not updated. The loop continues to the next element.
6. If the condition is false, it means that the current element is greater than or equal to the previous element, and the index `idx` is updated to the current index `i + 1`. The loop then breaks and exits the loop.
7. After the loop completes, the function returns the maximum value between the calculated index `idx` and -1 as the final answer.

Feel free to ask any questions if you would like further clarification on the solution!