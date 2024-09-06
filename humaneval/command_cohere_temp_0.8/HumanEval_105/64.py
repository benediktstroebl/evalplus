Here's a Python script that implements the `by_length` function:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reversed_sorted_arr = sorted(sorted_arr, reverse=True)
    names = []
    for num in reversed_sorted_arr:
        if num >= 1 and num <= 9:
            names.append(NAME_DICT[num])
    return names if names else []

# Dictionary to map digits to their names
NAME_DICT = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
             '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}

# Test cases
empty_arr = []
empty_result = by_length(empty_arr)

single_num = [8]
single_num_result = by_length(single_num)

multiple_nums = [2, 1, 1, 4, 5, 8, 2, 3]
multiple_nums_result = by_length(multiple_nums)

wrong_nums = [1, -1, 55]
wrong_nums_result = by_length(wrong_nums)

test_cases = {
    'empty_arr': empty_result,
    'single_num': single_num_result,
    'multiple_nums': multiple_nums_result,
    'wrong_nums': wrong_nums_result
}

# Print test results
for key, value in test_cases.items():
    print(f"Test Case: {key}")
    print(f"Result: {value}")
    print("=" * 50)
```

This script defines the `by_length` function, and uses a dictionary `NAME_DICT` to map digits to their names. It then defines some test cases and prints the results. The test cases include an empty array, a single number, multiple numbers, and some wrong numbers.