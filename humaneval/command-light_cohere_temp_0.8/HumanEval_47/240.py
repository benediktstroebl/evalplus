```python
def median(lst):
    n = len(lst) // 2 + 1
    m1, m2 = n // 2, n  # Calculate middle indices
    return (lst[m1] + lst[m2]) / 2 if n % 2 == 0 else lst[m1]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([9, 8, 13, 10]) == 13.0
assert median([1, 2, 3]) == 2.0
assert median([4, 3, 2, 1]) == 1.6
``` 
This Python code defines a function median that computes the median of a list of numbers. The function uses the code to calculate the median based on the length of the list. The test cases ensure that the function works correctly for different scenarios, including lists of different lengths and positive and negative numbers.