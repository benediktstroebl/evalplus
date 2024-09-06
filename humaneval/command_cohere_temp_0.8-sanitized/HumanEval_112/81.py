def reverse_delete(s, c):
    # Resultant String after deletion
    result = [x for x in s if x not in c]
    # Resultant String reversed
    reversed_result = result[::-1]
    # Check if the reversed resultant string is equal to the original string
    if reversed_result == s:
        return (''.join(result), True)
    else:
        return (''.join(result), False)