def exchange(lst1, lst2):
    """Determine if it's possible to make lst1 have only even numbers with exchanges.

    Args:
        lst1 (list): A list of integers.
        lst2 (list): Another list of integers.

    Returns:
        str: "YES" if possible to exchange for all even in lst1, otherwise "NO".
    """
    odd_in_lst1 = [x for x in lst1 if x % 2 != 0]
    return "YES" if len(odd_in_lst1) <= len(lst2) else "NO"