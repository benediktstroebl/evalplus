
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    elif n < 4:
        return False
    else:
        arr = []
        for i in range(1, n):
            if i % 2 == 0:
                arr.append(i)

        for j in range(1, len(arr)):
            for k in range(j + 1, len(arr)):
                for l in range(k + 1, len(arr)):
                    for m in range(l + 1, len(arr)):
                        if arr[j] + arr[k] + arr[l] + arr[m] == n:
                            return True

        return False
