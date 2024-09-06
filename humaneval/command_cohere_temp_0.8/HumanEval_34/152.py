```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in set function to remove duplicate elements from the input list and then uses the sort function to sort the unique elements. 

To ensure that the function meets the problem requirements, let's test it with a sample input and an expected output:
```python
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
expected_result = [0, 2, 3, 5, 9, 123]
result = unique(test_list)
print(f'Input list: {test_list}')
print(f'Expected Result: {expected_result}')
print(f'Actual Result: {result}')
```
The output should show that the function unique solves the problem correctly:
```
Input list: [5, 3, 5, 2, 3, 3, 9, 0, 123]
Expected Result: [0, 2, 3, 5, 9, 123]
Actual Result: [0, 2, 3, 5, 9, 123]
``` 
This demonstrates that the function unique sorts and removes duplicate elements from the input list, as per the problem statement. 
Let me know if any additional guidance or support is needed! I am available to help further refine the function to best suit your requirements. P.S. Feel free to introduce additional test cases to verify the functionality of the unique function.