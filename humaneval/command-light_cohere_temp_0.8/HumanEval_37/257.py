```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return even + [x for x in lst if x % 2 == 1]

# Test the function
even = sort_even([5, 6, 3, 4])
print("even:", even)

# Test the function with an empty list
even = sort_even []
print("even:", even)

# Test the function with list of odd numbers
even = sort_even([10, 11, 12])
print("even:", even)
```
The function `sort_even` is designed to transform a list into another list. It works by creating a list called `even`, which includes elements from the original list that are even numbers. Then, the function returns `even` and appends to it the elements from the original list that are odd numbers. The script also includes a series of tests to validate the function.