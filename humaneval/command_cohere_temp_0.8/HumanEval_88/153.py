```python
def sort_array(array):
    odd, even = sorted(array), sorted(array, reverse=True)
    return odd if sum(array[0], array[-1]) % 2 else even
```

The script uses basic conditional logic to sort the array and then returns the appropriately sorted array based on the sum of the first and last index values. It achieves this by using a ternary conditional operator to decide between 'odd' and 'even' sorting based on whether the sum of the first and last index values is odd or even, respectively. 

This script fulfills the requirement of not modifying the original array and provides the sorted array according to the specified conditions. 
```python
odd, even = sorted(array), sorted(array, reverse=True)
```
This line effectively prepares both the ascending and descending versions of the array in a more efficient way rather than creating two separate loops.