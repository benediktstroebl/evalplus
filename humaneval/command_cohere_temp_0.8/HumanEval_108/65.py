```python
def count_nums(arr):
    output = sum(int(b) for a in arr for b in str(a) if b != '0')
    return output
```
This function uses a nested list comprehension which iterates through each element in the list and each digit in the string representation of the element. It counts all integers that have a digit that is not equal to 0 and returns the count. 

This should satisfy the test cases mentioned in the problem statement.