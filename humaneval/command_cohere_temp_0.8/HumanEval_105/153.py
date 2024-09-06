```python
def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = filtered_digits[::-1]
    names = []
    for num in reversed_digits:
        names.append(str('Zero' if num == 0 else 'One' if num == 1 else 
                          'Two' if num == 2 else 'Three' if num == 3 
                          else 'Four' if num == 4 else 'Five' if num == 5 
                          else 'Six' if num == 6 else 'Seven' if num == 7 
                          else 'Eight' if num == 8 else 'Nine' if num == 9 
                          else 'Invalid' )))
    return names if names else []
```

The provided Python script solves the problem statement as explained below:
1. First, it sorts the array of integers `arr` only considering numbers between 1 and 9. 
2. Then it reverses the resulting array of digits.
3. Finally, for each digit in the reversed digit array, it corresponds a name ranging from "Zero", "One", ..., "Nine" and adds it to a list that is later returned.

Note that the script handles optional tests specified in the problem statement, such as returning an empty list if the input array is empty and only returning the names of numbers that are between 1 and 9 if there are other numbers present in the array. 

This solution is efficient and should work well for large inputs considering that the sorting operation takes O(n log n) and the rest of the operations are linear with respect to the size of the array.