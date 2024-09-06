```python
def strange_sort_list(lst):
    # Ensure list is sorted in descending order and contains at least two elements
    if len(lst) < 2:
        return lst
    min_val = min(lst)
    max_val = max(lst)
    return [min_val] + [max_val] + strange_sort_list(lst[:-2])
```

This function leverages recursion, which is a method where the solution to a problem is based on solving smaller instances of the same problem. This is achieved by defining the solution in terms of smaller or similar instances of the same problem. In this case, the function strange_sort_list() solves a problem in terms of a smaller instance of the same problem, which is the list without the last element. The base or smallest instance is when the list contains less than two elements, which returns the list as is.

The steps carried out by the function are the following:
1. The function starts with the smallest possible subset of the list, which is the list itself.
2. Then, it appends the smallest element to the result.
3. Subsequently, it appends the largest element to the result.
4. Finally, it applies the function to the remaining list (excluding the two extreme values) and appends the result to the current result.

The function stops when the list to be processed lacks two elements, which is the smallest instance. The base case of the recursion is when there is only one or no element left, where the function simply returns the list as is.

To better understand this, let's take a practical example using strange_sort_list([1, 2, 3, 4, 5]):
1. The function first takes the list with all elements, [1, 2, 3, 4, 5].
2. It sorts it and extracts the smallest element, which is 1.
3. Then, it sorts and extracts the largest element, which is 5.
4. Now, the list becomes [1, 5], and it is passed to the function again.
5. The process keeps going until there are no elements left. The final result will be [1, 5, 2, 4, 3].

This logic achieves the described strange sort order, with the final result containing the smallest, largest, and the sorted remaining elements.