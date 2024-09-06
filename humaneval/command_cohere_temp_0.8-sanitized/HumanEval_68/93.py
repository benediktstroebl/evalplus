def pluck(arr):
    # Find the smallest even value in the array
    even_value = min(x for x in arr if x % 2 == 0)
    
    # Use a lambda function to find the index of the chosen value
    index_of_even_value = lambda x: arr.index(x)
    
    # Return the plucked node in the list format specified in the prompt
    return [even_value, index_of_even_value(even_value)]