```python
def sort_third(l: list):
    """Sorts a list l such that values at indices that are not divisible by three are in l're original order, while values at indices that are divisible by three are sorted.
    
    This function returns a result list l' whose elements are:
    - elements at indices that are not divisible by three in l remain in l's original order.
    - elements at indices that are divisible by three are sorted in ascending order.
    """Example usage:>> [1, 2, 3, 5, 6, 7, 8, 9] 
    [2, 3, 5, 6, 7, 8, 9]"""
    l = [1, 2, 3, 5, 6, 7, 8, 9]
    l = sort_third(l)
    print(l)
    ```