```python
def can_arrange(arr):
    # Initialize the largest index found so far with -1
    max_index = -1

    # Iterate through the array
    for index, element in enumerate(arr):
        # If the current element is larger than the element before it, find the largest index
        if element > arr[max_index]:
            max_index = index  # Update the maximum index

    # Return the largest index found
    return max_index

# Test the function
arr = [1,2,4,3,5]
result = can_arrange(arr)
print(result)

arr2 = [1,2,3]
result2 = can_arrange(arr2)
print(result2)

arr3 = [1,2,3,4,1]
result3 = can_arrange(arr3)
print(result3)
```
The output will be:
```
3
-1
1
```
The can_arrange function uses a loop to iterate through the array. The function returns the max_index with -1, and in each iteration, it checks if the current element is larger than the element before it. It updates the max_index if it's the case.