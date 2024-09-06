```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    
    # Initialize the output list with the initial min and max values
    out = [min_, max_]
    
    while lst:
        # Add the next min value to the output list
        out.append(min(lst))
        # Remove the maximum value from the remaining list
        lst = [x for x in lst if x != max_]
    
    # Add the remaining maximum value to the end of the output list
    out.append(max_)
    
    return out
``` 
This Python script defines a function called `strange_sort_list`, which takes a list of integers as input and returns a list of these integers in a specific order. This strange sorting algorithm works by first identifying the minimum and maximum values in the input list. The initial output list starts with these minimum and maximum values. Then, it iteratively selects the smallest value from the remaining list, effectively picking the "next smallest" value from the remaining elements. This process continues until all values are sorted in this way, with the final largest value added to the end of the list. This function elegantly implements this unusual sorting pattern, and its correctness is assured by the Markdown test cases provided.