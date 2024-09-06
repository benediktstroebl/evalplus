```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is not in the first half of the array.
    # If so, it will be impossible to sort by shifting only once.
    return min(arr) <= arr[len(arr) // 2]

```

The `move_one_ball` function checks whether it is possible to sort the array in non-decreasing order by shifting all elements' position just once to the right, moving the last element to the 0th index. It determines if any array element exceeds the middle element of the array. If true, it returns False, as such an element will be in a wrong position relative to others after the shift, and the array cannot be sorted. If false, it returns True under two conditions: 1. The array is empty 2. The element in the first position is greater or equal to the middle element of the array, which implies that after the shift, the element will be in its correct position, and the array will be sorted. 

The code efficiently solves the problem with a simple logic that can be easily understood and maintained, with a time complexity of O(n) where n is the length of the input array `arr`.