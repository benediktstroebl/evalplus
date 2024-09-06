```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = lst[0]
    max_ = lst[0]
    
    # Sort the list in the "strange" way
    for num in lst[1:]:
        if num > max_:
            max_ = num
        elif num < min_:
            min_ = num
    
    return [min_, max, min_, max_] + [num for num in lst if num > max and num < min_]
``` 

The function works as follows: 

1. The function takes a list of integers `lst` as input. 
2. It initializes the `min_` and `max_` values with the first element of the list. 
3. It then iterates through the list, comparing each element to the `min_` and `max_` values. 
4. If the element is greater than the current `max_`, it becomes the new `max_`. 
5. If the element is less than the current `min_`, it becomes the new `min_`. 
6. The list is then rebuilt with the `min_`, `max_`, and `min_` values, and all elements that are greater than the `max_` and less than the `min_`. 

The resulting list is returned. 

Note, that lists with an even number of elements will have a repetitive element in the middle, e.g. `strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]`. 

Also, this solution is not suited for empty lists.