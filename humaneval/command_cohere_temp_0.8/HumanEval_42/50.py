Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and increment it by 1, and the result is a new list with the incremented elements. 

To test this function, you can run the following code:
```python
test_list = [1, 2, 3]
result = incr_list(test_list)
print(result)
```
This should print out:
```
[2, 3, 4]
```
Which is the expected result. 

This function should also work correctly for any list input, including duplicates, as demonstrated in the original problem description.