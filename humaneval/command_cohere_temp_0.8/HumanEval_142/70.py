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
This function traverses the list using the enumerate function to access both the index and value of each entry. It applies the corresponding operation for squaring or cubing based on the index being a multiple of 3 or 4. The sum is then computed and returned as the result. 

Here's an example usage of the function:
```python
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
print(sum_squares([]))  # Output: 0
```
This should produce the desired output as specified in the problem, which is the sum of squares for each multiple of 3 and the sum of cubes for each multiple of 4 (not including 3).