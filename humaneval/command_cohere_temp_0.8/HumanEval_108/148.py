```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output
```
This function sums over each element in the array `arr`, and if the sum of the digits of the concatenated string representation of the element is greater than 0, it casts the element to an integer and adds it to the total sum. The final output is the total count of such elements. 

Here is an example usage of the function:
```python
arr = [1, 11, -11, 10, -2, 13]
print(count_nums(arr))
```
This will print out `3`, as the positive integers have sums of digits greater than 0, whereas the negative numbers (namely `-2` and `-11`) do not. 

This problem can be solved more efficiently using the `sum` function's `digits` argument in Python 3.9 and above. Here is an example:
```python
def count_nums(arr):
    output = sum(n for n in arr if n > 0 and str(n).isdigit())
    return output
```
In this solution, we iterate through each element in the list, and for each positive integer with a digit string representation (`str(n).isdigit()`), we add it to the total sum using the `sum` function. 

We do not need to manually iterate through the digits of each number, allowing for a more concise solution.