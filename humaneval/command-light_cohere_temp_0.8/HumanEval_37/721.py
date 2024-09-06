```python
def sort_even(lst):
    # Define a new list to hold the sorted even values
    even = [x for x in lst if x % 2 == 0]
    
    # Sort the even elements of the list
    sorted_even = sorted(even)
    
    # Return the new list with sorted even values
    return sorted_even

# Unit tests for the function sort_even
test_sort_even = [
    # Test with a list of odd elements
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    # Test with a list of even elements
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
]
``` 
This code defines a function, `sort_even`, that takes a list as input and returns a new list with the even elements sorted. The function first creates a list, `even`, which contains the elements from the input list that are divisible by 2. Then, it sorts the elements of the `even` list and returns the sorted list.