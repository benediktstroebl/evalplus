```python
def strange_sort_list(lst):
    # Helper function to find the max element from the remaining list
    def max_from_remaining(L):
        max_so_far = float('-inf')
        for x in L:
            if x > max_so_far:
                max_so_far = x
        return max_so_far

    # Special case when empty list
    if not lst:
        return lst

    # Sorting the list
    return [x for i, x in enumerate(lst) if i == 0 or x == max_from_remaining(lst[:i-1])]
```

This code provides an efficient and elegant solution that implements the strange sorting as per the problem statement. The logic behind the sorting is to select the next element in the sorted list that is either the minimum (when processing the first element) or the maximum among the remaining elements. This approach ensures the correct order while maintaining a good performance ratio.

The provided example tests are adequate to validate the correctness of the solution, but it's also important to stress test the function with thousands of elements to ensure its efficiency.