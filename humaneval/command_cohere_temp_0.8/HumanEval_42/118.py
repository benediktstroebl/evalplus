Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

The script passes the given tests as the function's behavior matches the specified problem statement. You can verify this by conducting tests on the provided test lists, which will return the desired results. 
```python
# Test the function
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
Feel free to use this function to solve your specific problem or as a building block for more complex operations. If you have any other questions or need further assistance, let me know! It's important to note that the original script you provided with the function incr_list did not have any validation or testing logic. I added tests to demonstrate how you can verify the correctness of the function for different inputs. Feel free to add more tests to cover a wide range of scenarios and ensure the function's correctness in various cases.