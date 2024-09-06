```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[int((n-1) / 2)]

#Test cases
assertEqual(median([3, 1, 2, 4, 5]), 3)
assertEqual(median([-10, 4, 6, 1000, 10, 20]), -10)
assertEqual(median([4, -20, -100, 2, 5]), 4)
assertEqual(median([-5, -10, -8, -3, 9]), -3)
```
This code defines a median function that calculates the median of a list. The function first checks if the median is an even number or odd number. If it's an even number, the function will return the average of the first and last elements. If it's a number, the function will return the middle element. The test cases validate the test the function by comparing the returned values with the correct median values.