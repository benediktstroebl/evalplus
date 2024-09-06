
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n = list(str(n))
    l = len(n)
    for i in range(1, l):
        if not n[i].isdigit() or n[i] not in ['0','2','4','6','8']:
            return False
    if n[0] == '0':
        return False
    if int(n[0]) % 2 != 0:
        return False
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for i in range(l):
        if n[i] == '0':
            l1.append(n[i])
            if l1.count(n[i]) == 2:
                return False
        elif n[i] == '2':
            l2.append(n[i])
            if l2.count(n[i]) == 2:
                return False
        elif n[i] == '4':
            l3.append(n[i])
            if l3.count(n[i]) == 2:
