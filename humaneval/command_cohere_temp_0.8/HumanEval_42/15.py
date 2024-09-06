Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. 

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
Which is the expected output, confirming that the function correctly increments each element in the list by 1. 

This function is self-contained and does not rely on any external variables or assumptions, which is the definition of a pure function. It also has a very clear and straightforward implementation, making it easy to understand and maintain. 

If you would like, I can provide additional examples of how this function can be called with different input lists to test its behavior further. Let me know if you need any more assistance.