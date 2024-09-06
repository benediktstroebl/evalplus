def even_odd_palindrome(n):
    """
    This function calculates the number of even and odd integer palindromes in the range from 1 to 'n', inclusive.
    
    Args:
        n (int): The upper limit (inclusive) for counting palindromes.

    Returns:
        tuple: A tuple containing two counts (int): one for even palindromes, and one for odd palindromes.
    
    """
    # The range from 1 to n + 1 (inclusive) in which we will count palindromes.
    count_range = range(1, n + 1)
    
    # Count even palindromes: Take half of the odd count, reasoning explained in the comment below.
    even_count = (len(count_range) - len(set(count_range))) // 2
    
    # Count odd palindromes: Remove even counts from the total count, then add back one to include odd counts.
    odd_count = len(count_range) - even_count + 1
    
    # Return the counts as a tuple
    return (even_count, odd_count)
n = 5