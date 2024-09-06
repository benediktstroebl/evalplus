```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    count = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            count += 1
    return count
```

This function `count_nums` takes an array of integers as input and returns the number of elements in the array that have a sum of their digits greater than 0. The function achieves this by first converting each element in the array to an integer using a list comprehension. It then iterates through each integer in the list, checks if its digits' sum is greater than 0, and if so, increases the count variable by 1. Finally, it returns the count.

This solution is efficient with a time complexity of O(n), where n is the length of the input array, as it checks each element in the array only once to evaluate its digit sum.