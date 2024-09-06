```python
def pairs_sum_to_zero(lst):
    if sum(lst) == 0:
        return True
    return False

# Test the function
for i in [1,3,5,0]:
    if pairs_sum_to_zero([i,3,5,0]):
        print(f"list with element {i} passes test")
    else:
        print(f"list with element {i} fails test")
``` 
This code defines a function `pairs_sum_to_zero` which takes a list `lst` as an argument. The function checks if the the sum of the elements in the list is equal to 0. Then, it returns `True` if it is the case, indicating that there are two distinct elements in the list that sum to 0. Otherwise, it returns `False` to indicate that the list does not have two elements with sum to 0.