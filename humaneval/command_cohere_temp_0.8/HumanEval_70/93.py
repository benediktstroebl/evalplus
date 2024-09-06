```python
def strange_sort_list(lst):
    # Output list
    out = []

    # Helper function to recursively sort the list
    def strange_sort(li):
        # Base case: If the list is empty, return it
        if len(li) == 0:
            return li
        # Otherwise, grab the minimum value and sort the rest
        else:
            minval = min(li)
            rest = li[li != minval]
            rest_sorted = strange_sort(rest)
            return [minval] + rest_sorted

    # Apply strange sorting
    return strange_sort(lst)
```

This Python script defines a function called `strange_sort_list` taking in a list of integers, aiming to return the list in a "strange" order: it starts with the smallest value, then the largest value among the remaining integers, then the smallest value among the remaining, and so on. The logic employs a helper function (`strange_sort`) that recursively sorts the list while keeping this pattern in mind. The base case of this recursive function is an empty list, which returns itself. Otherwise, it finds the minimum value and sorts the rest using the strange sorting method. Ultimately, the main function calls `strange_sort` to sort the list and returns the sorted result.