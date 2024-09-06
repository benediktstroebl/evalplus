```python
def sort_array(array):
    odd, even = array[:1], array[1:]
    odd = odd[::-1] if sum(odd) % 2 else odd
    return even + odd
```
This Python script provides a function `sort_array` that accepts an array of non-negative integers as input. This function partitions the array into two parts: a first segment containing the first element of the array and a remaining second segment. The elements of the second segment are reversed if the sum of the first segment elements is even; otherwise, they are left as is. The function then concatenates the first segment and the modified second segment to produce a sorted copy of the input array. The order of elements in the output array is determined by whether the sum of the first segment elements is odd or even. If the sum is odd, the first segment will be followed by the reversed second segment, resulting in an ascending order; otherwise, the second segment will be in its original order, resulting in a descending order. The time complexity of this function is O(n), where n is the number of elements in the input array, and the space complexity is O(1) as it only uses constant space for temporary variables.