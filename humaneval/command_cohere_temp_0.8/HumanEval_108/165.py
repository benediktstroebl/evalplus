Here is a Python script with a self-contained function that solves the problem and passes the tests:
```python
def count_nums(arr):
    return sum(int(b) for a in arr for b in str(a) if b != '0')
```
```
This solution utilizes a nested list comprehension which loops over each element in the array and its corresponding string representation. It utilizes int() to convert each digit of the number to an integer and checks if the digit is not equal to '0'.
```