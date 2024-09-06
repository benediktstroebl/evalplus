```python
def max_element(l: list):
    max_element = max(l)
    return max_element
```

The function 'max_element' takes a list `l` as an input and returns the maximum element in the list using the `max` function to find the maximum value in the list. 

Here is an example of using the max_element function with a sample list:
```python
test_list = [1, 2, 3]
result = max_element(test_list)
print(result) # 3
```

The output of this code will be 3, which is the maximum element in the list [1, 2, 3]. 

This function is straightforward and effective, and it passes both test cases mentioned in the problem statement, as it assumes the presence of a maximum element in the list. 
If the input list is empty, the function will produce an error.  Thus, it's important to handle such cases accordingly depending on the specific requirements of the task.