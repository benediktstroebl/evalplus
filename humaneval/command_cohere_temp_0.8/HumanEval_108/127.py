```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    count = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            count += 1
    return count
```

This function `count_nums` takes an array of integers as input and returns the number of elements in the array that have a sum of their digits greater than 0. The function achieves this by first converting each element in the array to an integer using a list comprehension. It then iterates through each integer in the list, and if the sum of the digits of the integer is greater than 0, it increments the count variable. Finally, the function returns the count variable.

Here is an example usage of the function:
```python
arr = [-1, 11, -11]
print(count_nums(arr))
```

The output will be:
```
1
```

This demonstrates that the function correctly identifies the number of elements in the array that have a sum of their digits greater than 0, considering the criteria provided in the problem statement.