Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list as input and returns a new list with each element incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. 

To confirm the function's behavior, you can test it using the following code:
```python
test_list = [1, 2, 3]
result = incr_list(test_list)
print(result)
```
This will output:
```
[2, 3, 4]
```

Given the more general and diverse nature of the list in the prompt, the following would be the test for this scenario:
```python
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)
print(result)
```
This will output:
```
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The function incr_list handles any list input, as it iterates over the list and adds 1 to each element, regardless of their initial value.