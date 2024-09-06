Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. The expression `[x + 1 for x in l]` generates a new list with each element of `l` increased by 1. 

To confirm functionality, you can call the function with two test cases provided in the original problem statement:
```python
# Test case 1
input_list = [1, 2, 3]
result = incr_list(input_list)
print(result)  # Output: [2, 3, 4]

# Test case 2
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(input_list)
print(result)  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This will output the expected result on the first case and the second case.