def exchange(lst1, lst2):
    """
    Determine if it is possible to make lst1 an list of only even numbers by exchanging elements with lst2, 
    and return "YES" if successful, otherwise "NO".
    """
    if len(lst1) != len(lst2):
        return "NO"
    for i in range(len(lst1)):
        if lst1[i] & 1 != lst2[i] & 1:
            return "NO"
    return "YES"