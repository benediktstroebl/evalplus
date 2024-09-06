from itertools import accumulate, chain
def pluck(arr):
    # Calculate the even values and their indices
    even_values, indices = zip(accumulate(chain([0], arr, [0])), (i for i, n in enumerate(arr, 1)))
    
    # Find the smallest even value and its index
    smallest_even_index = next((i for i, n in enumerate(even_values) if n == min(even_values)), None)
    smallest_even_value = even_values[smallest_even_index]
    smallest_index = indices[smallest_even_index]
    
    # Return the result as a list
    return [[smallest_even_value, smallest_index]] if smallest_even_index is not None else []