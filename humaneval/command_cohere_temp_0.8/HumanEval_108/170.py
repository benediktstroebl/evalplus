```python
def count_nums(arr):
    nums = [int(i) for i in arr]
    counts = 0
    for n in nums:
        if sum(int(d) for d in str(n)) > 0:
            counts += 1
    return counts
```

This function takes an array of integers `arr` as input and calculates the number of elements in the array that have a sum of their digits greater than 0. It does this by first converting each element in the array to an integer using a list comprehension. It then initializes a count variable `counts` to 0.

It then iterates through each integer `n` in the list of integers, and checks if the sum of the digits of this number is greater than 0. If so, it increments the count variable. 

Finally, it returns the final count, counts. 

This function is standalone and can be executed with its corresponding test cases to verify its correctness. 

**NOTE**: This solution is based on the assumption that members of the array are integers and not floats. Although floats can also have digits, this solution only considers the whole numbers.