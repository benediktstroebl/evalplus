```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

The function sums over the list `lst` and for each entry, squares it if the index is a multiple of 3 and cubes it if the index is a 
multiple of 4 and not a multiple of 3. The result is then summed and returned. The code is encapsulated in a function for 
reusability and readability. 

The `enumerate` function is used for clearer indexing and the modulo operator is used to determine if an index meets the 
specified conditions. 

This approach allows for a clear division of responsibilities, separating the logic for squaring and cubing from the 
accumulation of the result, and follows the DRY principle. 

Note that this response does not cover the edge cases of an empty list or a list containing only negativities, as these 
were not included in the provided prompt. However, if you provide the additional edge cases, the code can be updated 
accordingly.