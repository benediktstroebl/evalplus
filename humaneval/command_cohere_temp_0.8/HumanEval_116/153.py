```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in a binary representation of a number, and the `sort_array` function sorts the array using a lambda function that prioritizes sorting keys based on the count of ones in their binary representation. The lambda function further uses `-n` to handle negative numbers correctly. The function passes the provided tests, indicating that it meets the problem requirements.  This approach optimizes the sorting process by using the binary representation of the numbers.  Overall, this solution is concise and efficiently implements the required sorting algorithm.