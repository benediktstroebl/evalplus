```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test case 1
input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(input_list)
print("Test Case 1:", end="flush")
print(result)

# Test case 2
input_list2 = [-1, 2, -4, 5, 6]
result2 = get_positive(input_list2)
print("Test Case 2:", end="flush")
print(result2)
```
This code defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the original list. 

It uses a list comprehension to filter out the negative numbers from the input.

The function is then tested with two different input lists, and the results are printed out.