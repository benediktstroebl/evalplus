```python
def sort_third(lst):
    """This function sorts a list so that values not divisible by three appear first.
    
    Args:
        lst (list) : list to be sorted
    """
    # sort list without third elements
    lst = [x for x in lst if x % 3 != 0] + [x for x in lst if x % 3]
    return lst

# Example usage:
print(sort_third([1, 2, 3, 4, 8, 9, 5, 6]))
 ``` 
This code defines a Python function named sort_third, which sorts a list lst so that values not divisible by three appear first. The function uses list comprehension to filter out elements that are divisible by three, and then combines these with the original list to produce a new list with the desired property. 
The example at the end demonstrates how the function works with a sample list.