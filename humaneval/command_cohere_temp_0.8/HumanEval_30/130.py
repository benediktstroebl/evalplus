Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for elements greater than zero, to return a list of all positive numbers in the input list `l`.

To test this function, you can use the following code:
```python
# Test 1
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

# Test 2
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
```
These tests check if the function returns the expected outputs based on the problem statement. 

The function can return only positive numbers from a given list of integers, regardless of whether the list contains thousands of elements or is empty. 
The current implementation is already optimal in terms of time and space complexity since it uses a simple list comprehension.