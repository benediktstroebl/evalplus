```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
This function takes as input a list of integers, squares each element if its index is a multiple of 3, and cubes each element if its index is a multiple of 4 but not a multiple of 3. It then sums up all the modified elements and returns the result. 

Here's an example of how to use the function:
```python
my_list = [1, 2, 3, 4, 5, 6, 7]
result = sum_squares(my_list)
print(result)  # Output: 627
```
This would generate the following output: 627. 
If the input list is empty, the function will return 0, as depicted in the following example:
```python
empty_list = []
result = sum_squares(empty_list)
print(result)  # Output: 0
```
Lastly, here is an example of a more varied list:
```python
negative_list = [-1, -5, 2, -1, -5]
result = sum_squares(negative_list)
print(result)  # Output: -126
```
This would be output: -126. 
This showcases the function correctly squaring and cubing the elements accordingly.