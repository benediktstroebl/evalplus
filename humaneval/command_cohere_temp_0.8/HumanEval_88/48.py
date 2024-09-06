```python
def sort_array(array):
    odd, even = array[:1], array[1:]
    odd, even = odd + reversed(even), sorted(even) if sum(odd + even) % 2 else reversed(even)
    return odd + even
```

This code divides the input array into two parts - the first element (odd) and all other elements (even). If the sum of the first and last element is even, it sorts the even elements in ascending order; otherwise, it sorts them in descending order. The order of the first element is then adjusted to maintain the correct order based on the sum of the first and last element. The resulting two subsets are then reassembled to produce the final sorted array. 

Such a solution takes advantage of the problem's constraint to sort efficiently based on the sum of the first and last index values.