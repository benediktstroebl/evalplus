
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
    # ord(char) returns a number
    # chr(number) returns a char
    # ord('a') == 97
    # ord('b') == 98
    # ord('z') == 122
    # chr(122) == 'z'
    
    # ord('A') == 65
    # ord('B') == 66
    # ord('Z') == 90
    # chr(65) == 'A'
    
    # ord('1') == 49
    # ord('2') == 50
    # ord('9') == 57
    # chr(57) == '9'
    
    # ord('0') == 48
    # chr(48) == '0'
    # ord('9') - ord('0') == 9
    
    def to_char(num):
        return chr(num + ord('0'))
    
    def to_num(char):
        return ord(char) - ord('0')
    
    def to_nums(lst):
        return [to_num(char) for char in lst]
    
    def to_chars(lst):
        return [to_char(num) for num in lst]
    
    def sort_coordinates(lst):
        return sorted(lst, key=lambda tup: (tup[0], tup[1]), reverse=True)
    
    def sort_row(lst):
        return sorted(lst, key=lambda num: -num)
    
    def get_row_coordinates(lst, x):
        """
        returns list of tuples [(x1, y1), (x2, y2) ...]
        """
        result = []
        for idx, row in enumerate(lst):
            # iterate over row
            for col_idx, char in enumerate(row):
                # if char == x:
                if char == to_char(x):
                    result.append((idx, col_idx))
        return result
    
    def get_row_coordinates2(lst, x):
        """
        returns list of tuples [(x1,
