```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach employs the built-in `sort()` method to arrange the list in ascending order. Subsequently, it verifies whether the length of the list is fewer than 2 or not. In the case where the list has fewer than two elements, next_smallest() returns None to indicate the absence of a second smallest element. Conversely, when the list encompasses at least two elements, the function returns the second element from the sorted list, serving as the next smallest number.

Here is a more detailed breakdown of the code:
1. **List Sorting**: The `sort()` method is employed to arrange the elements of the input list lst in ascending order. By doing so, the largest element is positioned at the first index (lst[-1]), and the smallest element is at the last index (lst[-2]).
2. **Length Check**: The script verifies the length of the sorted list. If the length is less than 2, implying a lack of distinct smallest and second smallest elements, the function returns None.
3. **Second Smallest Element**: In cases where the list possesses at least three elements, the function delivers the second smallest element, which is indexed at lst[-2]. 

This approach allows for an efficient and straightforward determination of the second smallest element, whilst also accounting for scenarios where no second smallest element exists.