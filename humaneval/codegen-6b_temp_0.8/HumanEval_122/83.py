
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
    def max_two(n):
        negative = n < 0
        n = abs(n)
        result = 0
        while n > 0:
            digit = n % 10
            result += digit
            n //= 10
        return -result if negative else result

    if len(arr) == 1:
        return arr[0]

    elements, index = arr[:k], 0
    current = max_two(elements[k - 1])

    while index < len(arr) - 1:
        if max_two(elements[k - 1]) == current:
            index += 1
            elements.append(arr[index])
        else:
            current = max_two(elements[-1])

    return sum(elements)

