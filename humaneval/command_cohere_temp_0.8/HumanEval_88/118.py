```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```

The code provides a `sort_array` function that takes an array of integers as input and returns a sorted copy of the array. It calculates the sum of the first and last elements of the array and checks if it's odd or even to determine the sorting order, using `odd = sum(array[0], array[-1]) % 2`. Then, it uses the `sorted` function, opting for the `reverse` keyword argument set to `odd` to sort the copy of the array in descending order if the sum is odd or in ascending order if the sum is even, returning the sorted array. Also, if the input array is empty, it returns the array as is since there is nothing to sort. 

This approach ensures that the original array remains untouched, and the sorted result is returned as expected based on the specified condition.