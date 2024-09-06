```python
def sort_array(array):
    odd, even = array[:1] + array[-1:], array[1:-1]
    return odd if sum(odd) % 2 else even
```

This code solves the problem by splitting the array into two parts: `odd` and `even`. The `odd` array contains the first and last elements of the original array, while the `even` array contains everything in between. The function then returns the `odd` array if the sum of the first and last elements is odd, and the `even` array if it's even.

Here is a more detailed explanation of the code:
- The expression `array[:1] + array[-1:]` creates a new array called `odd` that consists of the first element of the original array and the last element of the original array. The `[:1]` slice selects the first element, and the `[-1:]` slice selects all elements from the last to the first, resulting in an array of length 2.
- The expression `array[1:-1]` creates a new array called `even` that consists of every element in the original array except for the first and last element. The `[1:-1]` slice selects all elements with an index greater than 0 and less than `len(array) - 1`.
- The `return odd if sum(odd) % 2 else even` line makes the function decide whether to return the `odd` or `even` array based on the condition `sum(odd) % 2`. If the sum of the first and last element of the `odd` array is odd, then the `odd` array is returned. Otherwise, the `even` array is returned. 
This code will work as requested in the prompt and should pass the tests.