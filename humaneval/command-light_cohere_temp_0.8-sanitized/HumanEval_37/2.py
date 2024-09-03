def sort_even(lst):
    """Sorts a list such that all odd indexes are preserved, and the values at even indexes match the corresponding values of l, but with sorting."""
    return sorted(lst,key=lambda x:x if x%2 else x+1)