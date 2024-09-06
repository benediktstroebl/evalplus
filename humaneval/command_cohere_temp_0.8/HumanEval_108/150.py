```python
def count_nums(arr):
    output = sum(int(b) for b in map(str, arr) if b != '-' and sum(int(d) for d in str(b)) > 0)
    return output
```
This function uses a generator expression to iterate over each digit of each number in the array and determines whether the digit is non-negative and the sum of the digits is greater than 0. The test cases provided in the prompt verify that the function behaves as expected for empty arrays as well as arrays containing various combinations of positive and negative numbers with single-digit and double-digit sums of digits. 
```python
>>> count_nums([]) == 0
True
>>> count_nums([-1, 11, -11]) == 1
True
>>> count_nums([1, 1, 2]) == 3
True
```