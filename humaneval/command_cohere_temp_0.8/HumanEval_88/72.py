```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script sorts an array of non-negative integers based on the sum of its first and last elements, with odd sums sorted in ascending order and even sums sorted in descending order. The `sort_array` function takes an array as input and returns a sorted copy of the array, ensuring the original array remains unchanged.

Here is a more detailed explanation of the code:
1. The `odd = sum(array[0], array[-1]) % 2` line calculates the oddity of the sum of the first and last elements of the array. The `% 2` part ensures that odd will be 1 if the sum is odd and 0 if the sum is even. 
2. The `return sorted(array, reverse=odd)` line returns a sorted version of the array, with the `reverse` argument set to the value of odd. This will cause the array to be sorted in descending order if odd is 1 and in ascending order if odd is 0. 

This code elegantly solves the problem statement in an efficient and readable manner. Feel free to ask any follow-up questions or request further enhancements to the solution.