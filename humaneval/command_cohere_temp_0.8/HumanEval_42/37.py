Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, resulting in the output list. 

Here are some examples of how this function can be used:
```python
# Example 1:
input_list = [1, 2, 3]
result = incr_list(input_list)
print(result)
# Output: [2, 3, 4]

# Example 2:
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(input_list)
print(result)
# Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This function efficiently converts the input list into an incremented list without any additional logic or modifications.