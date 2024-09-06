
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # Use a map to store the numbers and their corresponding digits
    numbers = {}
    for i in arr:
        numbers[str(i)] = i
    # Check if all numbers have at most two digits
    for number in numbers:
        if len(str(number)) > 2:
            return 0
    # Find the sum of the elements with at most two digits
    for i in range(1, k):
        if numbers[str(arr[i])]:
            number = numbers[str(arr[i])]
            numbers[str(arr[i])] = 0
            numbers[str(number)] = 0
            # Multiply all numbers with 0
            for j in range(len(numbers)):
                if str(numbers[j]) != str(number):
                    numbers[j] *= 0
    return 0
