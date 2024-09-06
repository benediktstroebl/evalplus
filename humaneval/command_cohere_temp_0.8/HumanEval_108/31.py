```python
def count_nums(arr):
    output = sum(int(b) for b in map(str, arr) if b != '-' and sum(int(d) for d in str(b)) > 0)
    return output
```
This Python script defines the function `count_nums`, which takes an array of integers as input and calculates the number of elements whose digit sum is greater than 0. To do this, it uses a list comprehension that iterates through each element in the input array, converting it to a string and checking if the first character (which indicates the sign) is not '-'. For each such element, it calculates the sum of its digits using a generator expression within the sum function, which iterates through the characters in the string representation of the element and converts them to integers. If this sum is greater than 0, it increments the output variable by 1. Finally, the function returns the calculated output value, indicating the number of elements with a positive digit sum in the input array.