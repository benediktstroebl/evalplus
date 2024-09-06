Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a short way of writing a for loop, to create a new list with only the positive numbers from the input list `l`. The expression `x for x in l if x > 0` creates a new list with all the elements `x` in `l` that are greater than 0. 

You can use the function as follows to test it:
```python
test_list = [-1, 2, -4, 5, 6]
print(get_positive(test_list))
```
This will output:
```
[2, 5, 6]
```

You can also test it with a list that has more data types to demonstrate that it only filters the positive numbers from the list:
```python
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(test_list))
```
This will output:
```
[5, 3, 2, 3, 9, 123, 1]
```