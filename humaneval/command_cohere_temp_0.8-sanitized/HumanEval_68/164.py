def pluck(arr):
    # find the smallest even value in the entire array
    smallest_even_value = min(x for x in arr if x % 2 == 0)
    
    # find the smallest index of the even value in the array using collections
    even_index = next((i for i, x in enumerate(arr) if x == smallest_even_value), None)
    
    # return the result as a list [value, index] or [ ] if none found
    return [smallest_even_value, even_index] if even_index else []