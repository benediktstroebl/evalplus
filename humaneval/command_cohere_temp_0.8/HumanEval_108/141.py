Here is a Python script with a self-contained function that solves the problem and passes the tests:
```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```
The function `count_nums` iterates through the array and creates a string for each integer with the digits of that number and then converts those digits back to an integer to compute the sum. If the sum of the digits is greater than 0, it returns True, else it returns False. The total number of True values returned is the answer to the question. This solution has a time complexity of `O(n * log(max(a)))`, where `n` is the length of the array and `max(a)` is the maximum integer in the array.