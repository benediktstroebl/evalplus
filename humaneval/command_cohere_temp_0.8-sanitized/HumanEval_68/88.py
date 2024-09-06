from collections import *
def pluck(arr):
    # Create a counter to keep track of the smallest even value
    smallest_even_value = float('inf')
    index_of_smallest_even = -1

    # Use a dictionary to store the indices of the even values for faster lookup
    even_values = {}

    # Iterate over the array to find the smallest even value and its index
    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even_value:
            smallest_even_value = num
            index_of_smallest_even = i

        if num % 2 == 0:
            even_values[num] = i

    # If there are no even values, return an empty list
    if smallest_even_value == float('inf'):
        return []

    # If there is only one even value, return it with its index
    if len(even_values) == 1:
        return [smallest_even_value, index_of_smallest_even]

    # If there are multiple even values, sort the values and indices by value and pick the first one
    sorted_pairs = sorted(even_values.items(), key=lambda x: x[0])
    return [sorted_pairs[0][0], sorted_pairs[0][1]]