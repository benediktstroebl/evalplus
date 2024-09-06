
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    # My strategy to solve this problem was to get the count of each 1's
    # in a number in binary. So for 10101 in binary, the count would be
    # 2. I then created a dictionary that contains the number of 1's
    # as keys and the array elements as values. The values were stored
    # in a list. I then created a function that sorted the list based
    # on the keys, but added a tie breaker to sort the values.
    # This way, when there were two elements with the same number of
    # 1's, then they were sorted by the values.

    # Function to find the number of 1's in a number.
    def count_ones(number):
        num = 0
        while number:
            num += (number % 10)
            number = int(number/10)
        return num

    # Get the count of 1's in each number in the array.
    num_ones = []
    for number in arr:
        num_ones.append(count_ones(number))

    # Create a dictionary to store the number of 1's as a key and the
    # array value as the value.
    num_ones_dict = {}
    for i in range(len(num_ones)):
        if num_ones[i] in num_ones_dict:
            num_ones_dict[num_ones[i]].append(arr[i])
        else:
            num_ones_dict[num_ones[i]] = [arr[i]]

    # Sort the dictionary based on the keys.
    sorted_num_ones_dict = sorted(num_ones_dict.items())

    # Create a new array to store the sorted array.
    new_arr = []
    # Add the elements to the new array based on the key value.
    for value in sorted_num_ones_dict:
        for item in value[1]:
            new_arr.append(item)

    return new_arr

