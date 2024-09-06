def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    elif n == 1:
        return False
    
    # preparation for binary representation
    nBits = bin(n - 1).count('1')
    mostSignificantBit = (1 << (nBits - 1)) * (-1)
    
    # mapping of array elements to their MSB positions
    position = {num: i for i, num in enumerate(arr)}
    # sort the positions in descending order by their MSB
    sorted_position = sorted(position.items(), key=lambda x: (x[1] & mostSignificantBit, x[0]))
    # true if there exists a non-decreasing permutation
    return all(num <= position[max(arr)] for num, max_ in sorted_position)