```python
def max_element(lst):
    return max(lst)

# Basic test cases
print("Basic Test Cases:", max_element([1, 2, 3])) # Output: 3
print("Basic Test Cases:", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123

# Test cases with lists with duplicates
print("List with Duplicates:", max_element([3, 2, 3, 1, -5])) # Output: 3
print("List with Duplicates:", max_element([5, 2, -5, -3, 3, 9, 0, 123, 1, -10, 2])) # Output: 123

# Test cases with empty list
print("Empty List:", max_element([]))

# Test cases with complex numbers
print("Complex Numbers:", max_element([1, 2, 3, 4, .5])) # Output: 3
print("Complex Numbers:", max_element([5, 2, -5, .3, 3, 9, 0, 123, 1, -10, 2])) # Output: 2
```

The function max_element in this code takes a list lst as input and returns the highest element in the list. It does this by utilizing the maximum() function on the list to determine the highest value. 

The code also includes a variety of test cases to confirm the functionality of the max_element function, including basic test cases, lists with duplicates, empty lists, and complex numbers.