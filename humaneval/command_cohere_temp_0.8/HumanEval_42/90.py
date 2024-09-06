Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to iterate over each element in the input list and increment it by 1. The incremented values are then returned in a new list.

To test this function, you can run the following code:
```python
test_list = [1, 2, 3]
result = incr_list(test_list)
print(result)
```
This should print out:
[2, 3, 4]

Similarly, for a more complicated test case, the output would be:
[6, 4, 6, 3, 4, 4, 10, 1, 124]

These results match the examples provided in the problem statement. 
If you encounter any issues or have further questions, feel free to ask!  Let me know if you would like any other assistance with problems or anything else you might be working on.