```python
def by_length(arr):
    digits = sorted(arr, key=lambda x: 1 if x > 0 and x <= 9 else float('inf'))
    return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][::-1]*len(digits) if digits else []
```

The provided Python script defines a function `by_length` that takes an array of integers as input. It sorts the array using a custom sorting key to ensure that only integers between 1 and 9 are considered. Then, it reverses the sorted array and replaces each digit with its corresponding name from "One" to "Nine". The final result is a list where each element is a digit's name, and the length of the result is equal to the number of sorted digits. The function returns an empty list if the input array is empty. Also, elements that are not within the specified range (1 to 9) are ignored in the final result.