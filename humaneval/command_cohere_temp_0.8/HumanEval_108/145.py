```python
def count_nums(arr):
    return sum(int(num) > 0 for num in arr)
```
This function counts the number of elements in the array that have a sum of digits greater than 0. It uses a generator expression, int(num) > 0 for num in arr, which iterates through the array and evaluates each element's digit sum. The sum function then adds up the counts of all elements satisfying this condition. 

The function returns the total count of such elements in the array. This solution is concise and efficiently computes the count using the generator expression and sum function.