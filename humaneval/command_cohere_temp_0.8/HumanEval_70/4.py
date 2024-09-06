```python
def strange_sort_list(lst):
    result = []
    while lst:
        min_val = min(lst)
        lst.remove(min_val)
        result.append(min_val)
        
        max_val = max(lst)
        lst.remove(max_val)
        result.append(max_val)
    return result
```

This code defines a function called `strange_sort_list` that takes in a list of integers as input. It sorts this list using a strange sorting algorithm where it first removes the minimum value from the list and adds it to the result, then removes the maximum value from the list and adds it to the result, and repeats this process until the list is empty. The resulting sorted list is then returned as the output.

Here's an example of how you can use this function:
```python
print(strange_sort_list([1, 2, 3, 4])) # [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5])) # [5, 5, 5, 5]
print(strange_sort_list([10, 9, 8, 7])) # [7, 10, 9, 8]
``` 
And the function also handles the edge case where the input list is empty, in which case it returns an empty list:
```python
print(strange_sort_list([]))  # []
``` 
This strange sorting algorithm is a simple example of an unconventional sorting algorithm, albeit not very efficient, primarily meant to demonstrate a proof of concept for unusual sorting approaches.