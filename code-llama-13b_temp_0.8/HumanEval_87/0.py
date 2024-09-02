
def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    def list_to_dict(lst):
        d = {}
        for i in range(len(lst)):
            d[i] = lst[i]
        return d
    def sort_in_descending_order(d):
        d = sorted(d.items(), key=lambda x:x[1], reverse=True)
        return d
    def sort_in_ascending_order(d):
        d = sorted(d.items(), key=lambda x:x[0])
        return d
    def get_all_coordinates(lst, x):
        coordinates = []
        for i in range(len(lst)):
            if x in lst[i]:
                coordinates.append((i, lst[i].index(x)))
        return coordinates
    coordinates = get_all_coordinates(lst, x)
    d = list_to_dict(coordinates)
    d = sort_in_ascending_order(d)
    return list(d.values())
    
    
