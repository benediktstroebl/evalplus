```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    counts = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            counts += 1
    return counts
```

This function `count_nums` takes an array of integers as input and returns the number of elements in the array that have a sum of their digits greater than 0. The function achieves this by first converting each element in the array to an integer using a list comprehension. It then iterates through each integer in the list, checking whether the sum of its digits is greater than 0, and increments a counter each time this condition is met. Finally, it returns the final count of such numbers.

This solution is encapsulated in a standalone function, and should provide a correct solution to the problem as outlined in the test cases provided.