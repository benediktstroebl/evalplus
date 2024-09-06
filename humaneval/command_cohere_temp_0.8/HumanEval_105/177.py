```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(transf_map[num - 1])
        else:
            result.append(str(num))
    return result if result else []
```

The algorithm for solving this problem contains the following steps:
1. Sort the array `arr` using Python's built-in sorting mechanism, but leverage the `-1` flag at the end of the sorting process to reverse the resulting array. This will place the smallest element at the first position, and the biggest element at the last position.
2. Create a mapping dictionary named `transf_map` that will be used to map digits to their names. This will be used to pivot digits to their respective names.
3. Initialize an empty list named `result` which will be used to store the resulting transformed numbers.
4. Loop through the sorted array, and for each number check if it is within the range of 1 to 9, if so, pivot the number to its name using `transf_map`, if the number is not within this range, simply append it to the result list as is (in its digital form).
5. Return the list `result` if it is not empty, if the input array was empty, this function will also return an empty list.