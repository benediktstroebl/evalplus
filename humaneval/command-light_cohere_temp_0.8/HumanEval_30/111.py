```python
def get_positive(input_list):
    positive = [num for num in input_list if num > 0]
    return positive

# Test the function with different input scenarios
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Input list 1:", input_list1)
result_list1 = get_positive(input_list1)
print("Result list 1:", result_list1)

input_list2 = [5, 3, -5, 2, -3, 3, 9, 0, -123]
result_list2 = get_positive(input_list2)
print("Result list 2:", result_list2)

input_list3 = [-1, 2, -4, 5, 6]
result_list3 = get_positive(input_list3)
print("Result list 3:", result_list3)
```
The function get_positive does exactly what it sounds like: it returns a list containing only the positive numbers from the input list.