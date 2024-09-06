```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script provides a function called `next_smallest(lst)` that aims to find the second smallest element in a given list of integers `lst`. The function first sorts the input list in ascending order using the `sort()` method. Then, it checks if the length of the list is less than 2. If the list contains fewer than two elements, it returns `None` since there cannot be a second smallest element in such a list. Otherwise, the function returns the second element from the end of the sorted list, which is the second smallest element.

Here is a simple example to help you understand how this function works: let's consider the list `[3, 9, 2, 1, 7]` and use the `next_smallest` function on it. This is what would happen:
- The function sorts the list in ascending order: `[1, 2, 3, 7, 9]`.
- Since the list has more than one element (in fact, it has 5 elements), the function picks the second last element from the sorted list, which is `2`.
- The function returns `2` as the second smallest element in the original list.

Note that the function returns `None` if the list has less than two elements, as there would be no second smallest element in such a list. For example, if you use the function with the list `[4]`, it will sort the list and determine that there is only one element, so it will return `None`.