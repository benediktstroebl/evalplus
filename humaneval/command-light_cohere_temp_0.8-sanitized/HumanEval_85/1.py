def add(lst):
    """Given a non-empty list of integers lst. add the elements that that are at odd indices, 
    sum of the even indices will be 0"""
    return sum([i for i in range(2, len(lst)) if lst[i] % 2 == 0])