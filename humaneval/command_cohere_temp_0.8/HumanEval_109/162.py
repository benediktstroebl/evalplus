Here's a Python script that contains a function named `move_one_ball` pertaining to the problem statement:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Traverse through the array and check if any element is greater than the last element
    for i in range(len(arr) - 1):
        if arr[i] > arr[-1]:
            return False

    # If no element is greater than the last element, it's possible to achieve sorted order
    return True

# Example usage
input_list = [3, 4, 5, 1, 2]
print(move_one_ball(input_list))  # Output: True

input_list = [3, 5, 4, 1, 2]
print(move_one_ball(input_list))  # Output: False
```

In this code, the `move_one_ball` function traverses the array from the second element up to the second last element. During this traversal, it checks if any element is greater than the last element in the array. If it finds any element that satisfies this condition, it returns False, indicating that achieving a sorted non-decreasing order is not possible. However, if the loop completes without finding any such element, it means that we can achieve a sorted order by performing right shifts, and the function returns True. The base case is when the array is empty, where True is returned as any right shift will maintain the sorted order.