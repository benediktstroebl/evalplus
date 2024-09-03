```python
def strange_sort_list(lst):
    # Helper function to find the max element from the remaining list
    def max_from_remaining(L):
        max_so_far = float('-inf')
        for num in L:
            if num > max_so_far:
                max_so_far = num
        return max_so_far

    # Base case: If the list is empty, return it
    if not lst:
        return lst

    # Otherwise, return the minimum value followed by the max of the remaining list
    return strange_sort_list([min(lst), max_from_remaining(lst[1:])] + lst[2:])
```

This Python script provides a function called `strange_sort_list` that takes a list of integers as input. This function sorts the list in a 'strange' order: it starts with the smallest value, then immediately follows it with the largest value from the remaining elements, then takes the second smallest value and its corresponding largest value, and so on. The result is a list that alternates between the smallest and largest values of the remaining elements, ending with the remainder of the list in its original order.

The code employs a recursive approach, utilizing a helper function `max_from_remaining` to calculate the maximum value from the remaining list after each iteration. The base case handles an empty list, ensuring that it's simply returned without any processing. 

Overall, the approach is efficient given the fact that the in-place sorting isn't utilized and the problem's nature. The function's time complexity is O(nlog(n)) due to the recursive stack space used, not O(n^2) as one might expect with a purely iterative approach involving multiple iterations through the list.