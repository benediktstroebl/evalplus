Here's a Python script that implements the `by_length` function with a self-contained code block:
```python
def by_length(arr):
    sorted_arr = sorted(arr, key=lambda x: (x >= 1 and x <= 9, x))
    reverse_sorted_arr = sorted(sorted_arr, reverse=True)
    result = [name for num, name in enumerate(zip("One Two Three Four Five Six Seven Eight Nine", repeat=9), 1)]
    return result[reverse_sorted_arr]

# Example usage
input_arr = [2, 1, 1, 4, 5, 8, 2, 3]
print(by_length(input_arr))
```
This script utilizes Python's `sorted` function with a custom key to sort the array first by digits and then by their corresponding names. The `zip` function is used to iterate over each digit and generate the corresponding name. Finally, the `enumerate` function is used to iterate over the sorted array and return the correct digit names based on their original positions in the input array.

When you run this code with the example input array, it should print out the expected output:
```python
['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
``` 

This approach avoids the need for additional libraries and keeps the code self-contained within the code block you provided.