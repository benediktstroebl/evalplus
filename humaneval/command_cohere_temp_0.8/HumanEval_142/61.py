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
This function takes as input a list of integers, squares each integer at index multiples of 3, cubes each integer at index multiples of 4 but not equal to multiples of 3, and leaves other integers unchanged. The function then returns the sum of all entries. 

Here is an example usage of the function:
```python
print(sum_squares([1, 2, 3]))
```
This will output: 6, as expected, as integers at index 0 and 3 are squared, and the sum of [1, 4, 9] is indeed 6. 

This is a simple example of problem solving using dynamic programming with steps:
1. Understand problem requirements and examples provided.
2. Determine the nested loops needed, in this case, a single nested loop by index.
3. Create a variable to hold the sum, initialized to 0.
4. Use the `enumerate` function to iterate through lists and determine the action to take based on index modulos. 
5. Determine the appropriate operation to take and accumulate the sum. 

This is a simple example that provides a framework for solving list-based problems in Python.