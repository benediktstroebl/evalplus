```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```

This solution uses a nested list comprehension that takes each element in the array and converts it to an integer to pass it to the sum function. It counts the elements that have a sum of digits greater than zero. The result is the total number of elements in the array that meet this criterion. The given test cases pass with this solution.