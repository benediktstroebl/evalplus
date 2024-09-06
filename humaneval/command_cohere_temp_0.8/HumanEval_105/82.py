```python
def by_length(arr):
    sorted_arr = sorted(arr)
    sorted_arr = sorted_arr[::-1]
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(NUM_TO_NAME[num])
        else:
            result.append(str(num))
    return result

NUM_TO_NAME = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
```

The provided Python script defines a function `by_length` that takes an array of integers as input and performs a series of operations to transform the array into a desired format.

1. The input array is first sorted in ascending order using the `sorted` function.
2. The sorted array is then reversed using slicing, `[::-1]`, to obtain the sorted array in descending order.
3. The function iterates through the reversed sorted array and performs the following steps for each integer:
   - If the integer is between 1 and 9 inclusive, it is replaced with its corresponding name from the `NUM_TO_NAME` dictionary. This mapping allows each digit to be represented by its full name.
   - If the integer is not within the range of 1 to 9, it is left as is (converted to a string during the iteration).

The final result is a list where each integer between 1 and 9 is replaced by its name, and other integers are retained as strings. The function returns this resulting list.

The `NUM_TO_NAME` dictionary is defined outside of the function and maps integer values 1 to 9 to their respective full names. This dictionary is used during the iteration to provide the naming functionality.

Overall, the script solves the problem statement by sorting the array, reversing it, and then processing each element to assign names or leave them as-is based on the criteria provided.