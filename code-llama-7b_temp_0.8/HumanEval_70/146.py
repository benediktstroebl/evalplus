
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if lst == []:
        return []
    else:
        a = lst[0]
        b = lst[1]
        c = lst[2]
        d = lst[3]
        if lst == []:
            return []
        elif d > a and c > b:
            return [a, b, c, d]
        elif a > d and b > c:
            return [d, c, b, a]
        elif a > b and d > c:
            return [b, a, c, d]
        elif b > a and c > d:
            return [a, c, b, d]
        elif a > c and b > d:
            return [c, b, a, d]
        elif a > d and b > c:
            return [c, d, a, b]
        elif c > a and b > d:
            return [a, d, c, b]
        elif c > d and a > b:
            return [b, a, d, c]
        elif c > b and a > d:
            return [b, d, a, c]
        elif b > c and a > d:
            return [c, a, b, d]
        elif b > d and a > c:
            return [c, d, b, a]
        elif a == b and b == c and c == d:
            return [a, b, c, d]
        elif b == a and a == c and c == d:
            return [a, b, c, d]
        elif c == a and a == b and b == d:
            return [a, b, c, d]
        elif a == c and c == b and b == d:
            return [a, b, c, d]
        elif b == a and a == d and c == b:
            return [a, b, c, d]
        elif a == d and d == b and c == a:
            return [a, b, c, d]
        elif d == a and a == c and b == d:
            return [a, b, c, d]
        elif a == c and c == d and b ==
