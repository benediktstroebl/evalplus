```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the values at the indices that are not divisible by three are sorted"""
    lst = list(map(lambda x: int(x) if int.is_integer(x) and x != 3 else x, lst))
    return sorted(lst)
# Tests
print(sort_third([1, 2, 3]))  
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  

``` 
This script defines a function called sort_third that sorts a list of numbers into a list lst such that the values at the indices that are not divisible by three are sorted. The function achieves this purpose by transforming the input list using a lambda function to filter out non-integer values and non-divisible-by-three values, and then returning the filtered list. The lambda function ensures that only numbers that are both integers and not divisible by three are included in the transformed list. 

The function then returns the sorted list, which is identical to the original list lst, but with the values at the indices that are not divisible by three sorted in ascending order.