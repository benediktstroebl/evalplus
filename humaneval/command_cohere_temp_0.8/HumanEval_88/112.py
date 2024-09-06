```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:] if array == [] else sorted(array)
    return sorted(array, reverse=True) if array != [] else array
```
This Python script defines a function `sort_array` that takes an array of non-negative integers as input. The function copies the input array without modification if it's empty; otherwise, it sorts the array in the following way:
1. If the length of the array is odd, it sorts the array in ascending order (smallest to largest).
2. If the length of the array is even, it sorts the array in descending order (largest to smallest).

The key insight here is that the parity of the array's length determines the sorting order, with odd parities leading to ascending sorting and even parities leading to descending sorting. This logic is encapsulated within the `sort_array` function, making it convenient to sort arrays based on this specific criteria.