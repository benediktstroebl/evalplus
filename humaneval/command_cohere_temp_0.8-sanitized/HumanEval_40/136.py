def triples_sum_to_zero(lst):
    # Define the 2D list to store the elements and their indices
    arr = [[elt, idx] for idx, elt in enumerate(lst)]

    # Sort the list based on the elements
    arr.sort()

    # Initialize the flag to False for a valid result
    result = False

    # Apply the binary search which allows us to skip partitions with 2 elements
    for i in range(len(arr) - 2):
        if arr[i][0] + arr[i + 1][0] + arr[i + 2][0] == 0:
            result = True
            break

    return result