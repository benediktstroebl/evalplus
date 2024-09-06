```python
def count_nums(arr):
    output = sum(int(num) >= 0 for num in arr)
    return output
```
This function uses a generator expression to iterate through each number in the array and determines whether its digits multiply to a positive value, using the int() function to convert each element to an integer. The sum function then adds up the quantities, returning the total count of elements that pass this test. This method avoids the creation of a large list for memory-intensive scenarios.