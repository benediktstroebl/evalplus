def get_row(lst, x):
    return [(row, len(row)) for row in lst if x in row and len(row) > 0]