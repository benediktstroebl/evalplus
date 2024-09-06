
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

    
    
    def get_coord(lst, x):
        """
        Returns coordinates of x in lst
        """
        
        coordinates = []
        
        for i, lst_of_columns in enumerate(lst):
            for j, column in enumerate(lst_of_columns):
                if x == column:
                    coordinates.append((i, j))
        return coordinates
    
    
    def sort_by_row(coordinates):
        """
        Sorts coordinates of the row by columns in descending order.
        Also, sort coordinates of the row by rows in ascending order.
        
        Examples:
        sort_by_row([(2, 3), (2, 4)]) == [(2, 3), (2, 4)]
        sort_by_row([(2, 3), (0, 3)]) == [(0, 3), (2, 3)]
        """
        
        sorted_coordinates = []
        
        for coordinate in coordinates:
            if coordinate[0] not in sorted_coordinates:
                sorted_coord
