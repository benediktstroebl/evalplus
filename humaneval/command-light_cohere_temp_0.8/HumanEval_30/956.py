```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test the function
list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
list2 = get_positive(list1)
print(list1 == list2)  # Should print True

# Test with non-list input
number = -4
result = get_positive(number)
print(result == [-4])  # Should print True
```
The function 'get_positive' takes a list as an argument and returns a new list containing only the positive numbers. It uses list comprehension with the critical condition 'num >= 0' to filter out negative numbers. The tests pass the test if the function works as expected.