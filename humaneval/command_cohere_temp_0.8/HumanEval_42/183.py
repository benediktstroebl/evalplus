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
Which is the expected output, confirming that the function correctly increments each element in the list by 1.  If you want to test the function with more complex examples, you can experiment with different input lists to see how the function behaves. 
```python 
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)
print(result)
```
This will give the following output:
```
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
Which is the expected output, demonstrating the functionality of the `incr_list` function in the context of both simple and complex test cases.