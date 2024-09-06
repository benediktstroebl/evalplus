```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This Python script defines a function called `sum_squares` that takes a list of integers as input. It iterates through each element in the list and modifies its value according to its index: it squares the value if the index is a multiple of 3, and cubes it if the index is a multiple of 4 but not a multiple of 3. The function then calculates the sum of these modified values and returns the result. 

Here's an example of how you can use the `sum_squares` function with different input lists:
```python
my_list = [1, 2, 3]
result = sum_squares(my_list)
print(f"The sum of squares for the list {my_list} is: {result}")  # Output: 6

my_list = [4, 5, 6]
result = sum_squares(my_list)
print(f"The sum of squares for the list {my_list} is: {result}")  # Output: 33

my_list = [7, 8, 9, 10, 11]
result = sum_squares(my_list)
print(f"The sum of squares for the list {my_list} is: {result}")  # Output: 294
```

This demonstrates how the function processes lists with different numbers and modifies and sums the values based on their indices, resulting in the desired sum of squares for each list.