Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

To test this function, you can call it with various lists and verify that the output list contains the expected values. 

For example:
```python
# Test 1
input_list = [1, 2, 3]
result = incr_list(input_list)
print(result)  # Output: [2, 3, 4]

# Test 2
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(input_list)
print(result)  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script will yield the correct output for the provided tests as per the problem statement. The function incr_list returns the list with elements incremented by 1. 
 incr_list([1, 2, 3]) -> [2, 3, 4]
 incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) -> [6, 4, 6, 3, 4, 4, 10, 1, 124]

However, this is not the most efficient code possible since it uses a list comprehension, which creates a new list from scratch, resulting in additional memory usage. Instead, you could optimize it by using the same list and updating elements directly to save memory. Here's an alternative version:
```python
def incr_list_optimized(l: list):
    l[:] = [x + 1 for x in l]
    return l
```
This version takes the input list l and uses the slice notation []= to update the list in-place, meaning that the original list is modified directly without creating a new one. This saves memory when dealing with large lists. For the same reason, it also avoids creating an empty list that would result in garbage collection afterward. 
```python
# Test 1
input_list = [1, 2, 3]
incr_list_optimized(input_list)
print(input_list)  # Output: [2, 3, 4]

# Test 2
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
incr_list_optimized(input_list)
print(input_list)  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
``` 
Both versions of the function incr_list and incr_list_optimized will yield the same results, but incr_list_optimized uses the optimized in-place update technique to achieve better performance and less memory consumption.  By avoiding creating a new list from scratch, it reduces memory usage and potentially improves the speed of the operation, especially for large input lists.  This will enhance the performance and the efficiency of the code.