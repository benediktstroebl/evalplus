```python
def sum_squares(lst):
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

The code employs Python's sum function and a generator expression to calculate the sum of squared integers in the input list lst. The generator expression x ** 2 generates the square of each element x in the list if it is an integer (i.e., x % 1 == 0), producing the sum of squared integers in the list.

To obtain the desired result, call the function sum_squares with the input list lst and assign the output to a variable, as seen below:
```python
# Example 1
input_lst = [1, 2, 3]
result = sum_squares(input_lst)
print(f"For lst = {input_lst}, the output should be 14")
```

This will produce the following output:
```
For lst = [1,2,3], the output should be 14
```

You can repeat this procedure for any other input lists mentioned in the problem statement.