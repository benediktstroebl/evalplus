Here's a Python script that solves the given problem with an efficient approach using `itertools.accumulate` and `collections.Counter`:
```python
from collections import Counter
from itertools import accumulate

def pluck(arr):
    even_sum = sum(x for x in arr if x % 2 == 0)
    indices = Counter(accumulate(arr))
    smallest_index, _ = indices.most_common(1)[0]
    return [even_sum, smallest_index] if even_sum != 0 else []
```
The approach uses some powerful Python features such as `itertools.accumulate` and `collections.Counter` to solve the problem efficiently. Here's a breakdown of the code:
1. `even_sum = sum(x for x in arr if x % 2 == 0)`: This line calculates the sum of all even values in the array. This is done using a generator expression, which is a concise way to create a list in memory.
2. `indices = Counter(accumulate(arr))`: This line uses the `accumulate` function to create a list of cumulative sums of the array. This list represents the indices of the array elements. The `Counter` class is then used to create a dictionary-like object that counts the occurrences of each element.
3. `smallest_index, _ = indices.most_common(1)[0]`: This line uses the `most_common` method of the `Counter` object to get the most common element (in this case, the smallest even value). The `most_common` method returns a list of tuples, with the most common element coming first. We retrieve the smallest index from the tuple. 
4. `return [even_sum, smallest_index] if even_sum != 0 else []`: This line returns the result if there is a valid pluckable node, or an empty list if there are no even values in the array. 

This approach efficiently calculates both the sum of even values and the smallest index without needing to iterate over the array multiple times, thus providing a time complexity of O(N), where N is the length of the input array.