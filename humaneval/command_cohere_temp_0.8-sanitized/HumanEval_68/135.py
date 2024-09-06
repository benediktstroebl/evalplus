def pluck(arr):
    # find the smallest even value in the entire array
    smallest_even_value = min(x for x in arr if x % 2 == 0)
    
    # find the smallest index of the smallest even value in the array
    smallest_index = arr.index(smallest_even_value)
    
    return [smallest_even_value, smallest_index]