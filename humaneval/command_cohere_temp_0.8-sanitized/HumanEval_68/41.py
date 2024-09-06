def pluck(arr):
    # find the smallest even value in the whole array
    smallest_even_value = min((x for x in arr if x % 2 == 0), key=lambda x: x)

    # find the index of the smallest even value in the whole array
    smallest_even_index = arr.index(smallest_even_value)

    return [smallest_even_value, smallest_even_index]
arr = [4, 2, 3]