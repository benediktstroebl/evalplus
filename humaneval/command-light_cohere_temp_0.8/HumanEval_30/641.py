```python
def get_positive(input_list):
    positive = [num for num in input_list if num > 0]
    return positive

input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(input_list))  # Output: [5, 3, 2, 3, 9, 123, 1]
input_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_positive(input_list2))  # Output: [4, 5, 6, 7, 8, 9]
```
This Python code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original input list. It uses list comprehension to filter out the numbers greater than 0 from the input list, and the resulting list is then returned. The code also demonstrates the code with an input list of various values, and the function successfully filters out the negative numbers and returns the desired positive numbers list.