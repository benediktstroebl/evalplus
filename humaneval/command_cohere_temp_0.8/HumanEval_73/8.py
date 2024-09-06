```python
def smallest_change(arr):
    arr = list(set(arr))
    return sum([1 for i in range(len(arr)) if arr[i] != arr[len(arr) - 1 - i]])
```

The function `smallest_change` works by first removing all duplicated elements in the input array using the `set()` method, which allows it to focus on the uniqueness of elements in the array and their ordering. It then checks if the first half and second half of the array have the same elements in reverse order, and counts how many elements need to change to match them. To do this, it uses a list comprehension where it iterates through the indices of the array and compares the element at that index with the corresponding element in the second half of the array (`arr[len(arr) - 1 - i]`), calculating the difference between them and returning a count of the elements that need to change. 

This approach ensures that the function dynamically analyzes the array and determines the minimum number of changes required to make it palindromic, satisfying the prompt requirements.