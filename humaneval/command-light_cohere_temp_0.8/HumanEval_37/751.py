```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted."""
    return [x if x % 2 != 0 else x[0] for x in l]

# Test the function
test_even = sort_even([5, 6, 3, 4])
print("Sorted list using odd index:", test_even)
print("Should be:", [[3, 6, 5, 4]])
```
The function `sort_even` takes a list `l` as an argument and returns a new list `l'`. This list `l'` contains elements from the original list `l` that are equal to the elements at the even index of the original list `l`, but sorted. 

The function works by iterating through each element of the original list `l`. For each element, it checks if the element is even (i. If the element is even, it swaps the element with its corresponding element at the even index of the original list `l`. If the element is odd, it keeps the element as is, because the original list `l` already has the element at the even index in the correct position. 

The output of the code block should be:
>  [3, 6, 5, 4]