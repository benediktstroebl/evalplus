
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = 0
    odd_count = 0
    # We do not use the % operator as we do not want to count the last digit which can be 0
    # for all numbers.
    while num > 0:
        # if num % 10 == 0:
        #     count += 1
        # else:
        #     odd_count += 1

        # We simply remove the last digit, by dividing the num by 10.
        # If num is 0, we would have reached the condition break and
        # hence this loop will not run.
        if num % 10 == 0:
            count += 1
        else:
            odd_count += 1

        num = num // 10
    return count, odd_count

