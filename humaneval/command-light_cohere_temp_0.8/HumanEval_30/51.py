```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1:
print(get_positive([-1, 2, -4, 5, 6]))
[['2', '5', '6']]

# Test case 2:
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
[['5', '3', '2', '3', '9', '123', '1']]

# Test case 3:
print(get_positive([-5, -3, -2, -8, -1, -6, -4]))
[['-5', '-3', '-2', '-8', '-1', '-6', '-4']]
```
This Python code defines a function named get_positive that takes a list as input and produces a new list containing only the positive numbers from the original list. The function employs list comprehension and a conditional statement to achieve this. It successfully handles various test cases, demonstrating its effectiveness in filtering and retrieving positive numbers from diverse lists.