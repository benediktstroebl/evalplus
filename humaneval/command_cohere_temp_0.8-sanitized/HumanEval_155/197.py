def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp = str(num)
    if temp[0] == '-':
        temp = temp[1:]
    for char in temp:
        if char > '9' or char < '0':
            if char == '-':
                continue
            else:
                count_odd += 1
        else:
            if int(char) % 2 == 0:
                count_even += 1
    return (count_even, count_odd)