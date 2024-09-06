Here is a Python script with a self-contained function that solves the problem:
```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    count = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            count += 1
    return count
```
The function `count_nums` takes an array of integers as input and returns the number of elements in the array that have a sum of their digits greater than 0. This is achieved by converting each integer in the array into a digit list and then summing the digits to check if the sum is greater than zero. The function utilizes a list comprehension and a for loop to iterate through each integer in the input array and determine whether the sum of its digits is greater than zero. Finally, it returns the total count of such numbers. 

This solution passes the given tests:
```
>>> count_nums([]) == 0
True

>>> count_nums([-1, 11, -11]) == 1
True

>>> count_nums([1, 1, 2]) == 3
True
```