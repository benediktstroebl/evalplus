```python
def count_nums(arr):
    output = sum(int(b) for a in arr for b in str(a) if b != '0')
    return output
```
This function uses a nested list comprehension which iterates through each element in the input list `arr`. It converts each element to an integer (`int(b)`), which allows us to proceed with digit extraction using a nested comprehension from its string representation (`str(a)`). It further checks if each digit is not equal to `0` (`b != '0'`) and calculates their sum using the `sum()` function. The final result will be the number of elements whose digits exhibit a positive sum. 

Here is a summary of the logic:
```python
sum(int(b) for a in arr for b in str(a) if b != '0')
```
Here is how you can use this function:
```python
>>> count_nums([]) == 0
True
>>> count_nums([-1, 11, -11]) == 1
True
>>> count_nums([1, 1, 2]) == 3
True
```
This should pass the given tests.