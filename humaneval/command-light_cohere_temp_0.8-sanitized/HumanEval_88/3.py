def sort_array(array):
    array.append(array[::-1])  # Reverse the elements
    array.sort()  # Sort the plain array
    return array