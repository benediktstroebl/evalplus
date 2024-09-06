```python
def by_length(arr):
    sorted_arr = sorted(arr)
    stripped_arr = [str(ele) for ele in sorted_arr if 1 <= ele <= 9]
    stripped_arr.reverse()
    digit_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [name for name, num in zip(digit_names, stripped_arr) if num != '' ]
```

The provided Python script sorts the array of integers between 1 and 9, reverses it, and replaces each digit with its name. It ignores any number not within the specified range. To ensure clarity, let's break down the code into its constituent components:
1. **def by_length(arr)**: This line defines a new function called `by_length` which takes one parameter, `arr`, which is the array of integers we'll be processing.
2. **sorted(arr)**: This line sorts the input array in ascending order using Python's built-in `sorted` function. After sorting, the array `arr` becomes `sorted_arr`.
3. **stripped_arr = [str(ele) for ele in sorted_arr if 1 <= ele <= 9]**: Here, we are creating an empty list called `stripped_arr` and using a list comprehension to populate it. For each element in `sorted_arr` (which is already sorted), we're checking if the element is between 1 and 9. If it is, we convert it to a string (using `str(ele))` and add it to `stripped_arr`.
4. **stripped_arr.reverse()**: This line reverses the order of elements within the `stripped_arr` list. After this operation, the `stripped_arr` becomes reversed, containing the digits in reverse order.
5. **digit_names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']**: This line creates a list of the names of the digits between 1 and 9. This list is used to replace the corresponding digits in the `stripped_arr`.
6. **return [name for name, num in zip(digit_names, stripped_arr) if num != '']**: Here, we use another list comprehension, this time to iterate over each element in `digit_names` and the corresponding element in `stripped_arr`. We only include a digit if it's not an empty string ('') - meaning that we ignore any odd digits. After this process, we end up with a list of names, which is then returned as the final result. 

This function will appropriately sort, reverse, and rename digits within the specified range, while ignoring any numbers outside of this range.