Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to increment each element in the input list by 1 and provide a result. It avoids modifying the original list and uses a simple and efficient approach. 
The expected output for the provided test cases would be:
```
[2, 3, 4]
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
Let me know if this solution suits your needs or if you have any other questions!