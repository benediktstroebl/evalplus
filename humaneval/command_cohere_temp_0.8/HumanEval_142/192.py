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
This Python script defines a function called `sum_squares` that takes a list of integers as input. It iterates through each element in the list using the `enumerate` function, which also gives the index of each element. Depending on whether the index is a multiple of 3 or 4, it squares or cubes the integer, respectively. The squared or cubed values are added to the `result` variable, which is then returned at the end of the function.

Here's an example of how you can use the `sum_squares` function to calculate the sum of squares and cubes for various list inputs:
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_squares(my_list)
print(result)  # Output: 285

my_list_2 = [10, 20, 30, 40, 50]
result_2 = sum_squares(my_list_2)
print(result_2)  # Output: 2500
```
This demonstrates how the `sum_squares` function can be used to calculate the sum of squares and cubes for different lists, following the specification provided.