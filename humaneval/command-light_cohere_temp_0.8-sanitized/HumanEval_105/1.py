def by_length(arr):
    if not arr:  # Check for empty array
        return []

    # Sorting the integers between 1 and 9
    valid_numbers = list(range(1, 10))
    arr = [num for num in arr if num in valid_numbers]

    # Reverse the array
    reversed_arr = arr[::-1]

    # Replace each digit with its name
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    reversed_str = ''.join(map(lambda x: names[int(x)], reversed_arr))