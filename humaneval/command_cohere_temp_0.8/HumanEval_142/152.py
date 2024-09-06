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
This function takes as input a list of integers and squares each integer at an index that is a multiple of 3 and cubes each integer at 
an index that is a multiple of 4 but not a multiple of 3. It leaves other integers unchanged and calculates the sum of all entries 
in the list. The function returns the sum of all entries in the list. 

Here is an example usage of the function:
```python
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
```
This, along with the accompanying test cases, should correctly match the example usage described in the problem.