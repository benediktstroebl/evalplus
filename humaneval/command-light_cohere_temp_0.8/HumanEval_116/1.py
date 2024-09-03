```python
def sort_array(arr):
    """
    Sorts the array of integers in a way that corresponds to the number of ones
    in the binary representation of the numbers.
    Returns an sorted array.
    """
example:
    >>> arr = [1, 5, 2, 3, 4]
    >>> sort_array(arr) == [1, 2, 3, 4, 5]
    >>> arr = [-2, -3, -4, -5, -6]
    >>> sort_array(arr) == [-6, -5, -4, -3, -2]
    >>> arr = [1, 0, 2, 3, 4]
    >>> sort_array(arr) == [0, 1, 2, 3, 4]
    """
    arr.count_ones = ['.boukas(arr).count_ones = sum([i for i in arr])
    return sorted(arr, key=lambda x: -count_ones)

def boukas(arr):
    """
    Returns the count of ones in binary representation of arr.
    """
    return bin(sum(1 for i in arr))[2:].count()

arr = [1, 5, 2, 3, 4]
print("Sorted array:", end="")
print(sort_array(arr))
``` 
This script defines a function called sort_array, which sorts an array of integers based on the number of ones in their binary representation. The boukas function calculates the count of ones in binary representation, and the sorted function sorts the array based on the count of ones.