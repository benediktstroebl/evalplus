```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    counts = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            counts += 1
    return counts
```

This function `count_nums` takes an array of integers as input and returns the number of elements in the array that have a sum of their digits greater than 0. The function achieves this by first converting each element in the array to an integer using a list comprehension. It then iterates through each integer in the list, checking whether the sum of its digits is greater than zero. If it is, the `counts` variable is incremented. Finally, the function returns the value of `counts`.

This solution is concise and straightforward, and it should efficiently handle any valid input. I hope this helps! Let me know if you have any further questions or if you'd like me to help with any additional problems you may have.