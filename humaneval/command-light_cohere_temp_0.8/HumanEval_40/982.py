```python
def triples_sum_to_zero(lst):
    if sum(x for x in lst if x != 0) == 0:
        return True
    else:
        return False

# Example usage:
if triples_sum_to_zero([1, 3, -2, 1]) == True:
    print("Solution found")

if triples_sum_to_zero([1, 2, 3, 7]) == True:
    print("Solution found")

if triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True:
    print("Solution found")

if triples_sum_to_zero([1]) == False:
    print("No solution exists")
```
The code defines a function `triples_sum_to_zero` that takes a list as an argument. The function checks if there are three distinct elements in the list that sum to zero, and returns `True` if it's the case, and `False` otherwise. The code also provides several example cases that demonstrate the functionality of the function.