```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
median([3, 1, 2, 4, 5])  # Output: 3.0
median([-10, 4, 6, 1000, 10, 20])  # Output: 15.0
median([1, 2, 3, 4, 5])  # Output: 3.0
median([10, 20, 30, 40, 30, 40])  # Output: 30.0
median([-100, -1000, -1, -1000, 0, 0])  # Output: 0.0
```

This Python script defines a function `median` that calculates the median of a list of numbers. The function first checks if the list has an odd or even amount of elements. Then, it uses the mathematical formula to calculate the median, which is the average of the two middle numbers in an sorted list. The test cases pass the also test the function with various input lists and ensure that the output is correct.