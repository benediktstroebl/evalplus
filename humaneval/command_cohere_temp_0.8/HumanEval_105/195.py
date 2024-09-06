```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(NUM_TO_NAME[num])
        else:
            result.append(str(num))
    return result

# Dictionary to map number to name
NUM_TO_NAME = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}

# Test Cases
empty_list = []
test_cases = [
    ([2, 1, 1, 4, 5, 8, 2, 3], ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']),
    ([], ['']),
    ([1, -1, 55], ['One', 'Five', '55']),
]

for tc in test_cases:
    assert by_length(tc[0]) == tc[1]
```

The provided Python code defines a function called `by_length` that sorts, reverses, and then converts digits 1 through 9 in an input array to their corresponding names. For non-digit values or numbers outside the range, they are directly appended to the result array. The script also features a `NUM_TO_NAME` dictionary mapping digits to their respective names. Test cases are included to validate the function against various scenarios, ensuring accurate transformation of arrays into sorted, reversed, and named representations.