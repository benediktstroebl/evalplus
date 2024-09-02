
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    result = []
    while num != 0:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = math.floor(num / 2)
        result.append(1)
    return (even_count, odd_count)

result = even_odd_count(num)
print(result)