Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to iterate over each element in the input list and increment it by 1. The new incremented list is then returned as the result. 

To test this function, you can run the following code:
```python
test_list = [1, 2, 3]
result = incr_list(test_list)
print(result)
```
This should print out:
```bash
[2, 3, 4]
```
If you need to test it with a more complicated list, you can use the following:
```python
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)
print(result)
```
This will output:
```bash
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
Thus, the function correctly solves the problem as stated in the original markdown code block.