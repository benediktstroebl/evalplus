```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
    }.get
    result = [transf_map(elem) for elem in sorted_arr if elem <= 9 and elem >= 1]
    return result if result else []
```

The script employs a dictionary named `transf_map` to translate integer values into their respective names. This is done to simplify the process of translating each digit in the `sorted_arr` array into its named form. The `sorted` function is utilized to arrange the input `arr` in ascending order, and the `[::-1]` slicing operation flips the resulting array to ensure the digits are correctly sorted in reverse order.