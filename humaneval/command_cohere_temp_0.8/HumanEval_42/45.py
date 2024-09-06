Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list **l** and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, resulting in an incremented list. 

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
Another example test case could be:
```python
test_list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result2 = incr_list(test_list2)
print(result2)
```
This will output:
```
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The function passes both test cases from the statement and should handle any list input correctly. 
The function incr_list returns a new list with elements incremented by 1 without modifying the original list. 
Please note that the original list remains unchanged. 
If you no longer need the original list, you may consider using list comprehensions to create a new list without leaving any residual modifications. In your problem statement, you can add a note to mention that the function returns a new incremented list without modifying the original list. 
This will make your code more transparent and align with the principle of least surprise.