```python
def sort_array(array):
    odd, even = array[:1], array[1:]
    odd = odd[::-1] if sum(odd) % 2 else odd
    return even + odd
```
This Python script provides a function `sort_array` that accepts an array of non-negative integers as input. This function partitions the array into two sections: `odd` (the first element) and `even` (all other elements). The elements in the `odd` segment are reversed if the sum of the odd elements is even to ensure the correct order when combined with the `even` segment. The final order of elements is achieved by concatenating the `even` and `odd` segments, maintaining the original order for odd sum sums and reversing it for even sum sums, thus providing the desired sorted array.