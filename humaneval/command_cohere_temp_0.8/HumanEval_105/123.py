```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    result = []
    for num in sorted_arr:
        if str(num) in '123456789':
            result.append(getNum(num))
    return result if result else []

def getNum(num):
    return {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}[str(num)]
```

The function `by_length` sorts the array, reverses it, and then iterates over the resulting array, converting each integer to its corresponding name. The helper function `getNum` is used to convert a digit to its name. This solution assumes that the input array only contains valid digits between 1 and 9.

To test this code properly, ensure that the helper function `getNum` is defined correctly, and the dictionary keys are aligned with the desired output. Test cases covering edge scenarios, such as empty arrays, invalid inputs, and various numbers of input arrays, are recommended to verify the robustness of the solution.