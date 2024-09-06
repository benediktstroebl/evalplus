```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` uses the Python built-in sorted() function to sort the given list. The function then checks if the length of the list is less than 2, returning None if there is no second smallest element. If the list has at least two elements, the function returns the second element from the sorted list, which is the next smallest element. 

Here is a one-liner to solve the problem:
```python
lambda lst: min(set(lst) - {min(lst)}).index() + 1
```
And here is a version of the solution with explanations appended:
```python
def next_smallest(lst):
    """
    Returns the second smallest number in lst.
    Returns None if there is no second smallest number, i.e., if the list has less than two elements.
    """
    # Sort the list
    lst = sorted(lst)
    
    # If the list has less than two elements, return None
    if len(lst) < 2:
        return None
    
    # Return the second element in the sorted list
    return lst[1]
``` 

This script defines a function 'next_smallest()' that takes in a list of numbers as input and returns the second smallest number in the list. It first sorts the input list in ascending order using the sorted() function. Then, it checks if the length of the sorted list is less than 2. If so, it returns None, indicating that there is no second smallest number in the list. Otherwise, it returns the second element of the sorted list, which is the second smallest number. 

The script ensures that the function is well-defined for all possible inputs, including empty lists and lists with less than two elements, by returning None in those cases. 

The `next_smallest` function's simplicity and clarity make it an excellent choice for solving this problem. It is also highly efficient, as sorting the list only takes O(n log n) time, where n is the length of the list.