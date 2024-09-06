def pluck(arr):
    # Split the list into even and odd values lists
    even, odd = separate_evens_and_odds(arr)

    # If even list is empty, return the first value in the odd list
    if not even:
        return [odd.pop(0), 0]

    # If odd list is empty, return the first value in the even list
    if not odd:
        return [even.pop(0), 0]

    # If both lists have elements, find the smallest even value and its index
    smallest_value = float('inf')
    smallest_index = None
    for idx, value in enumerate(even):
        if value < smallest_value:
            smallest_value = value
            smallest_index = idx

    # Find the index of the smallest even value in the odd list
    odd_smallest_index = None
    for idx, value in enumerate(odd):
        if value < smallest_value:
            odd_smallest_index = idx
            break

    # Return the result depending on the existance of the index
    if odd_smallest_index:
        return [smallest_value, odd_smallest_index]
    else:
        return [smallest_value, smallest_index]
def separate_evens_and_odds(arr):
    even = []
    odd = []
    for value in arr:
        if value % 2 == 0:
            even.append(value)
        else:
            odd.append(value)
    return even, odd