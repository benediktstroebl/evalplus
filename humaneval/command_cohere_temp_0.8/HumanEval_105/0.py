Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x <= 9 else x)
    reversed_sorted_arr = sorted(sorted_arr, reverse = True)
    result = []
    for num in reversed_sorted_arr:
        if 1 <= num <= 9:
            result.append(NUM_TO_NAME[num])
    return result if result else []

NUM_TO_NAME = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9}
```

This script includes the `by_length` function that takes an array of integers as input and returns a list of named digits based on their length in the array. It first sorts the array such that all digits are moved to the beginning, then reverses this sorted array, and finally converts each digit into its name. The script also includes a dictionary `NUM_TO_NAME` for mapping digits to their respective names. This solution is self-contained and can be executed as standalone code.