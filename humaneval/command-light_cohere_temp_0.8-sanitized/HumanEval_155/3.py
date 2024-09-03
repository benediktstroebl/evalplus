def even_odd_count(num):
    """This function returns a tuple of number of even and odd digits in the given integer."""
    # Calculate and return count of even and odd digits
    return (len(str(num).find(isdigit)), len(str(num).find(isdigit)))