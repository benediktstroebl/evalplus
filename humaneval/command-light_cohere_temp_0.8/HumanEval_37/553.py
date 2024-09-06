```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted."""
    return sorted(l, key=lambda x: x if x % 2 == 0 else x-1)
``` 
This function uses the `sorted` function with a custom key lambda function to sort the list based on even or odd indices, depending on the condition of the index.