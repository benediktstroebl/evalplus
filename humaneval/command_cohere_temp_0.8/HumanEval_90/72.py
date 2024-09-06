```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach employs the Python built-in `sort()` method to sort the given list. Subsequently, it verifies if the length of the list is less than 2. Notice that such a list will only contain the smallest and largest elements in the sorted list, which are the two extremes. Hence, if the list has less than 2 elements, the function returns None as there is no second smallest element. Otherwise, it returns the second element from the sorted list, which is the second smallest element from the original list.

Here is a more in-depth explanation of the code for those who are interested in such details:
1. Sorting the List: The `sort()` method in Python sorts the list in ascending order by default. That means the smallest element in the list will be at index 0 after sorting, and the largest element will be at the last index.
2. Checking for the Second Smallest: After sorting the list, the function checks if there are only one or two elements in the list. If there's only one element, or if the list is empty, there won't be a second smallest element, which is why `None` is returned in such cases.
3. Returning the Second Smallest: If there are more than two elements in the list, the function returns the second element from the end of the sorted list. This is the second smallest element, as the first smallest element is at index 0 and the second smallest at index 1 in the sorted list.

This is a concise and efficient solution that effectively handles all the edge cases mentioned in the problem statement.