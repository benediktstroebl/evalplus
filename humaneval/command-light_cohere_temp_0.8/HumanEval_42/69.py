```python
def incr_list(lst):
    lst[:] = [1] + lst  # Move the head of the list to the end
    return lst

# Test the function with a list of values
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_incr_list)

# Print the result
print(result)
```

This code defines a function incr_list that takes a list lst as input and modifies it by shifting the head value to the end of the list. It then returns the For empty list [1] + lst to simulate the increment, which effectively moves the head of the list to the end. The test_incr_list list is then passed to incr_list and the result is printed.