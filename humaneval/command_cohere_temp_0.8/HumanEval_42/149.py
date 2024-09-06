```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
``` 

This Python script defines a function called `incr_list`. It takes a list l as input and returns a new list where each element is incremented by 1. The function uses a list comprehension to iterate over each element in the input list and adds 1 to it. 

Here's an example of how to use this function:
```python
my_list = [1, 2, 3, 4, 5]
result = incr_list(my_list)
print(result)
```

Output:
[2, 3, 4, 5, 6]

The function can also handle various input list data types and lengths. Here is an example:
```python
my_list_2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result_2 = incr_list(my_list_2)
print(result_2)
```

Output:
[6, 4, 6, 3, 4, 4, 10, 1, 124]

This shows that the function can handle different types of input lists and produces the expected results.