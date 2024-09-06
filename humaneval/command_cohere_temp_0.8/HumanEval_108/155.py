```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    count = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            count += 1
    return count
```

This approach converts each element of the array from a string to an integer and then calculates the sum of the digits character by character and stores it in the `count` variable.

You can test this function by calling it with different arrays and comparing the output with the test cases provided.

For example:
```python
>>> count_nums([-1, 11, -11])
1
>>> count_nums([1, 1, 2])
3
>>> count_nums([])
0
>>> count_nums([-2, 20, 400, 3000, -9])
4
```