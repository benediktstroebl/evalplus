```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

#Test cases
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Input list 1:", input_list1)
print("Output:", get_positive(input_list1))

input_list2 = [5, 3, -1, 7, -9]
print("Input list 2:", input_list2)
print("Output:", get_positive(input_list2))

input_list3 = [5, 3, 0, -6, 7]
print("Input list 3:", input_list3)
print("Output:", get_positive(input_list3))

input_list4 = [5, -5, 3, -3, 7]
print("Input list 4:", input_list4)
print("Output:", get_positive(input_list4))

input_list5 = [1, 2, -3, 4, 5, 6]
print("Input list 5:", input_list5)
print("Output:", get_positive(input_list5))
```
The function `get_positive` takes an input list and returns a new list with only the positive numbers. It uses list comprehension and `[]` to filter the numbers in the list based on the condition `num >= 0`.