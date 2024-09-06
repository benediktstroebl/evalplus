```python
def count_nums(arr):
    return sum(int(num) >= 0 for num in arr)
```
The function `count_nums` iterates through the array of integers, checking if each element is greater or equal to zero. It does so using the built-in Python function `int`, which casts the elements to integers, and the `>=` operator. Instead of explicitly checking the sum of digits, the code takes a more pragmatic approach to filtering out numbers with positive sums of digits. 

This solution has a time complexity of O(n), where n is the length of the input array, as it requires iterating over each element once.