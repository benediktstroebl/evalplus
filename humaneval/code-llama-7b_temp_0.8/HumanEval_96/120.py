
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """

    if n <= 1:
        return []
    arr = []

    # 0,1 and 2 are not prime numbers
    if n > 2:
        arr.append(2)

    if n > 3:
        arr.append(3)

    i = 0
    # i is the index of the element to be checked if it is a prime number or not
    # j is the index of the element that we want to divide the element at i by
    # in order to check if it is a prime number or not
    j = 0

    for i in range(0, n - 1):
        is_prime = True
        j = 0
        while j < i and is_prime:
            is_prime = i % arr[j]
            j = j + 1

        if is_prime:
            arr.append(i + 2)
    return arr
