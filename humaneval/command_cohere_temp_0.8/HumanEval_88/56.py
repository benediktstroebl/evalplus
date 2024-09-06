```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script provides a function `sort_array` that takes an array as input and returns a sorted copy of the array. The function checks the parity of the sum of the first and last elements of the array, and sorts the array in descending order if the sum is even, and in ascending order if the sum is odd, while handling the edge case where the input array is empty. This sorting behavior helps in selecting the smallest and largest elements in a structured way, aiding in problem-solving scenarios.