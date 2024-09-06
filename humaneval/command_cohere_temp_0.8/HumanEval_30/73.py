Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a compact way of creating a new list based on existing lists. In this case, it creates a new list that includes only the elements of l that are greater than zero. The resulting list contains elements x for which the condition x > 0 is true. 

To further explain list comprehension, here is an example of how you might call the function with a sample input and iterate through the resulting list:
```python
# Example call to the function
input_list = [-1, 2, -4, 5, 6]
result_list = get_positive(input_list)
print(result_list)  # Output: [2, 5, 6]

# Iterating through the result list
for item in result_list:
    print(item)
```
This would print:
```
2
5
6
```
As shown, the list comprehension feature of Python is a concise way to create a new list based on an existing one, which can be very useful when you need to filter or transform elements in a list. 

This function does not have the descriptive comments that were provided in the original problem statement, but it is a more concise way of solving the problem and obtaining the desired results. 
```python
def get_positive(l):
    return [x for x in l if x > 0]
```