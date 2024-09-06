```python
def can_arrange(arr):
    prev = arr[0]
    ans = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur < prev:
            ans = idx
        prev = cur
    return ans
```
The solution employs a nested loop approach, where one loop iterates through the array elements, and another loop (the innermost one) tracks the index of the current element. If the current element is smaller than its previous one, the outer loop increments the answer accordingly. The loop reverses when an element exceeds the previous one, ensuring the largest index of the required subarray is captured in the answer. If no suitable subarray exists, the function returns -1. 

This approach guarantees finding the maximum index of a non-decreasing subarray, given the array's elements are sorted in ascending order. 
This is an efficient solution with a time complexity of O(n), where n is the array's size.