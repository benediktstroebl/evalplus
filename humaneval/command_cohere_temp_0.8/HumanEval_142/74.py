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
The code uses a for loop to iterate through each index and corresponding value in the input list `lst`. The conditionals `i % 3 == 0` and `i % 4 == 0 and i % 3 != 0` determine whether to square or cube each number, respectively. Finally, the squared or cubed values are added to the result variable, which is then returned. 

To ensure the function is correct, three tests are performed: 

```python
# test the function
lst1 = [1, 2, 3]
assert sum_squares(lst1) == 6

lst2 = []
assert sum_squares(lst2) == 0

lst3 = [-1, -5, 2, -1, -5]
assert sum_squares(lst3) == -126
```

Each test case validates whether the function produces the expected output given the input.