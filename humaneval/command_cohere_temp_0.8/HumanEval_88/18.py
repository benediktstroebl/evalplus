```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that takes an array of non-negative integers as input. The function checks whether the length of the array is odd or even to decide whether to sort the array in ascending or descending order. Finally, it returns a sorted copy of the input array based on this criteria. 

This solution does not consider the complexities of the given examples as optimal as possible. Instead, it focuses on solving the problem in a straightforward manner.  If desired, there are other more optimized ways to implement this function.