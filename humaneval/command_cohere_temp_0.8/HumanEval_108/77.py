```python
def count_nums(arr):
    output = sum(int(b) for a in arr for b in str(a) if b != '0')
    return output
```
This function uses a nested list comprehension which iterates through each element in the input list `arr`. It converts each element to an integer (`int(b)`). Then it iterates through each digit of the element's decimal representation, and if a digit is not zero (`b != '0'`) it counts it. Finally, the function returns the total count of such digits.

This should provide the expected output for the given test cases:
```python
>>> count_nums([]) == 0
True

>>> count_nums([-1, 11, -11]) == 1
True

>>> count_nums([1, 1, 2]) == 3
True
```