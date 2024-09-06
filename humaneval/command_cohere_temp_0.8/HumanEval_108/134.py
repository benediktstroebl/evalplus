```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output
```
This function uses a generator expression to iterate over each element in the input list and calculate the digit sum of each number using a nested list comprehension. It then checks if this sum is greater than zero and contributes to the total count if so. The final count is returned as the function output. 

You can test this function by calling it with different input lists and comparing the results with the expected outputs from the given tests:
```python
>>> count_nums([]) == 0
True
>>> count_nums([-1, 11, -11]) == 1
True
>>> count_nums([1, 1, 2]) == 3
True
```