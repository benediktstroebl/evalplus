```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    numbered_arr = [str(elem) for elem in sorted_arr if 1 <= elem <= 9]
    named_arr = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][numbered_arr]
    return named_arr if named_arr else []
```

The provided Python script defines a function `by_length` that takes an array of integers as input and performs a series of operations to transform the array into a desired format. 

1. The function first sorts the input array in ascending order using the `sorted` function, but the sorting is done in reverse order due to the use of `[::-1]`. This results in an array of digits sorted in reverse order.
2. The function then filters out elements that are not between 1 and 9 using a list comprehension. It converts each element to a string representation, as the original problem statement requires string names.
3. Finally, the function looks up the index of each element in the sorted and filtered array in the list `[['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']]` and assigns the corresponding name. The list comprehension guarantees that the resulting named array will be sorted in the reverse order of the original input array.

Note that the code assumes that the input array only contains integers between 1 and 9, and any strange or non-numeric elements will be ignored. It returns an empty array if the input array is empty.