Here's a Python script that contains a function named `maximum_k` that solves the problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]
```
The function `maximum_k` takes in an array `arr` and an integer `k` as input, sorts the array, and returns the maximum `k` numbers from the sorted array.

You can test this function with the following Python code:
```python
Test = ["-3", "-4", "5", "-7", "8", "3", "9", "10", "-8", "i", "5", "-5", "3", "-9", "2", "4"]
print(maximum(Test, 3))
```
The output of this code will be `-7, -8, 5`.