```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The function `count_ones` is used to extract the number of ones in each number's binary representation which is then used as a criterion for sorting in the `sort_array` function. 

This approach allows the code to meet the problem specifications, as shown by the sample test cases provided. 
The function sorts the array first by the number of ones in the binary representation and then, for numbers with the same number of ones, it sorts them by their decimal value in descending order. 

This solution adheres to the problem's guidelines and provides a efficient and scalable approach.