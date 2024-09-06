```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    
    # Initialize the result list with the initial minimum value
    result = [min_]
    
    while lst:
        # Add the maximum value of the remaining list (excluding the just added min_)
        result.append(max(lst[:-1] if min_ == max_ == lst[-1] else lst))
        
        # Remove the added element from the list
        lst.remove(min_)
        
        # Update the min_ and max_ for the next iteration
        min_, max_ = max_, min_
    
    return result
``` 

The algorithm for solving this problem consists of the following steps:
1. Find the minimum and maximum values from the list.
2. Add the minimum value to the result list.
3. Iterate through the list again and again. In each iteration:
    - Find the maximum value of the remaining elements in the list (excluding the just added minimum).
    - Add the maximum value to the result list.
    - Remove the minimum value from the list.
    - Update the minimum and maximum values for the next iteration.

These steps repeat until the list is empty. 

The given example tests demonstrate how this algorithm sorts the list in the "strange" order as requested in the problem statement.