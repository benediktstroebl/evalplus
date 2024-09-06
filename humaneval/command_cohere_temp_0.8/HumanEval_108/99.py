```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(map(int, str(n))) > 0)
    return output
```

This function `count_nums` iterates over all the elements in the input array `arr`. For each element, it calculates the sum of its digits by converting it to a string and mapping each character to its integer representation. If this sum is greater than zero, it increments the output variable by 1. Finally, it returns this output variable, which will be the number of elements that have a sum of digits greater than zero. This algorithm has a time complexity of `O(n)` since it requires iterating through the array once and processing each element in constant time.