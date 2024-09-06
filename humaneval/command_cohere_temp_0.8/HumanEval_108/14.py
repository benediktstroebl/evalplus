```python
def count_nums(arr):
    output = sum(int(num) for num in arr if sum(int(d) for d in str(num)) > 0)
    return output
```
This function sums over all elements in the array `arr` and counts the number of elements where the sum of the digits is greater than 0. It does so by first converting the integer to a string, summing up the digits, and then converting the sum back to an integer. The overall time complexity of this function is `O(n log n)`, where `n` is the length of the input array. This is because the function iterates over each element in the array and performs a linear operation (converting the integer to a string, summing the digits, and converting the sum back to an integer).