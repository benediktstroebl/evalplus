def exchange(lst1, lst2):
    res = 'NO'
    # Check if any element of lst1 is odd
    if any(num % 2 for num in lst1):
        # Exchange odd numbers with even numbers from lst2
        lst1[:], lst2[:] = [num for num in lst2 if num % 2 == 0], [num for num in lst1 if num % 2 == 0]
        # Check if all elements in lst1 are even now
        if all(num % 2 for num in lst1):
            res = 'YES'
    return res