```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach utilizes Python's built-in sorting mechanism, `sort()`, which efficiently arranges the elements of the input list in ascending order. Subsequently, the code verifies the length of the list, returning `None` if there are only one or zero elements, since there is no clear second-smallest value in such cases. Conversely, if there are at least two elements, the function returns the second element from the sorted list, which corresponds to the second smallest element in the original list. 

Here is a more detailed breakdown of the code:
1. `lst.sort()`: This line sorts the elements of the input list lst in ascending order using the built-in `sort()` method. 
2. `if len(lst) < 2`: Checks if the length of the list is less than 2. If True, it means there is no distinct second smallest element, so the function returns None. 
3. `else`: This is the alternative branch of the if statement, which is executed when the condition is False. It means there are two or more elements in the list, so it returns the second element from the sorted list (`lst[-2]`). 

This approach provides a straightforward solution that adheres to the problem statement's guidelines and efficiently computes the second smallest element in a given list.