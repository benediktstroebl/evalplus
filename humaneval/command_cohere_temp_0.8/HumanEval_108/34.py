```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    count = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            count += 1
    return count
```

This function takes an array of integers `arr` as input and calculates the number of elements in the array that have a sum of their digits greater than 0. It does this by first converting each element in the array to an integer using a list comprehension. It then iterates through each integer in the list and checks if the sum of its digits is greater than 0. If it is, the count is incremented by 1. Finally, the function returns the total count of elements with the specified condition. 

This solution passes the provided tests as it correctly identifies the elements with positive digit sums in the given sample outputs.