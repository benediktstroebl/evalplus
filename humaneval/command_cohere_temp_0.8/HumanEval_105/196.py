```python
def by_length(arr):
    DIGS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    arr = sorted(arr) if arr else arr
    arr = [x for x in arr if 1 <= x <= 9]
    arr.sort(reverse=True)
    return [DIGS[i] for i in arr if i < len(DIGS)]
```

The provided Python script solves the problem using the following steps:
1. Assigns the digits from 1 to 9 as names in the `DIGS` list for easy referencing.
2. Checks for an empty array, returns an empty array if it is empty.
3. Sorts the array if it contains valid digits and ignores strange numbers.
4. Extracts the sorted elements from the array and converts them into their name representation, using the `DIGS` list.

This solution is efficient and can solve the problem for small to medium-sized arrays.