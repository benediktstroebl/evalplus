def reverse_delete(s, c):
    # Calculate the delted string
    deleted = ''.join([x for x in s if x not in c])

    # Check if the deleted string is a palindrome
    return (deleted, deleted == deleted[::-1])