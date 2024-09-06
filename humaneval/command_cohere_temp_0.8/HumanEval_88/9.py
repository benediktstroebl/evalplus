```python
def sort_array(array):
    odd, even = array[:1], array[1:]
    odd = odd[::-1] if sum(odd) % 2 else odd
    return even + odd
```
This Python script solves the problem by splitting the array into two parts: `odd` and `even`. The `odd` array contains the first element of the original array, and the `even` array contains the rest of the elements. 

If the sum of the elements in the `odd` array is odd, it means that the first element of the sorted array should be the largest, so `odd` is reversed. Otherwise, if the sum of the elements in the `odd` array is even, it means that the first element of the sorted array should be the smallest, so `odd` remains as it is.

The sorted odd elements are then concatenated with the `even` elements to form the final sorted array.

This solution is concise and uses subtle logic to solve the problem in an efficient manner. It can be tested for different cases to ensure it works correctly. You can use it in a Markdown cell by copying and pasting it into a cell and checking the results against the given test cases.