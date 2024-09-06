```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    count = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            count += 1
    return count
```

This function `count_nums` takes an array of integers as input and returns the number of elements in the array that have a sum of their digits greater than 0. The function achieves this by first converting each element in the array to an integer using a list comprehension. It then iterates through each integer in the list, and if the sum of the digits of the integer is greater than 0, it increments the count variable. Finally, the function returns the value of the count variable.

This solution is efficient and easily generalizable to any number of tests cases, as it simply loops through the input list and processes each integer sequentially to determine whether its digit sum is greater than zero. Thus, it has a time complexity of O(n), where n is the number of elements in the input array.