def by_length(arr):
    # Sort and reverse the list of integers from 1 to 9
    sorted_arr = sorted(arr)
    reversed_arr = sorted_arr[::-1]
    result = []

    # Convert each digit into its name and append to result
    for num in reversed_arr:
        if 1 <= num <= 9:
            result.append(PART_TO_NAME[num])

    return result if result else []
PART_TO_NAME = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
               '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}