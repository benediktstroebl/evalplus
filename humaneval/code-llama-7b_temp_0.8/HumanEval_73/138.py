
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # Taking an array with a length less than 2 is impossible
    if len(arr) < 2:
        return 0

    # Create a dictionary to store the occurrences of each number
    numbers = {}
    for number in arr:
        if number in numbers:
            numbers[number] += 1
        else:
            numbers[number] = 1

    # If there is a single number in the array, the minimum number is 0
    if len(numbers) == 1:
        return 0

    # Create a new dictionary to store the number of occurrences for each number
    occurrences = {}
    for number, amount in numbers.items():
        if amount in occurrences:
            occurrences[amount] += 1
        else:
            occurrences[amount] = 1

    # If there is only one number with an odd number of occurrences, we just need to check
    # if the total amount of occurrences is even or not
    if occurrences[1] == 1:
        return len(arr) % 2

    # We need to find the minimum number of even occurrences
    # to make the array palindromic
    even_occurrences = occurrences[2]
    if even_occurrences % 2 == 0:
        even_occurrences = even_occurrences // 2
    else:
        even_occurrences = even_occurrences // 2 + 1

    return len(arr) - 2 * even_occurrences
