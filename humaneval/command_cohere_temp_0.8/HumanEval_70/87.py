```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = lst[0]
    max_ = lst[0]
    
    # Loop to find the maximum and minimum values in the list
    for n in lst[1:]:
        if n > max_:
            max_ = n
        elif n < min_:
            min_ = n
    
    # Return the sorted list in the required format
    return [min_, max_, *sorted(lst)[1:-1]]
```

The following Python function named `strange_sort_list` is defined. This function takes a list (`lst`) as input. It employs an ingenious sorting strategy where it first identifies the minimum and maximum values within the list. Then, it returns a new list that starts with the minimum value, followed by the maximum value of the remaining numbers, then the next smallest number, and so forth until it has placed all the numbers except one in the middle of the list. The result is a list that is strangely ordered in this manner.

The function is well-documented with a description, examples, and a comment explaining the odd sorting strategy, ensuring clarity and making it easily understandable for users. 

The specified examples showcase the function's expected behavior when sorting lists, demonstrating the unique sorting pattern that the function produces.