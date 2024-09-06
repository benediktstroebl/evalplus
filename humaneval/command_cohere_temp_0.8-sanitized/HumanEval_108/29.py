def count_nums(arr):
    nums = [int(i) for i in arr]
    # Calculating the sum of digits for each number in the array.
    sod = [sum(map(int, str(j))) for j in nums]
    # Filtering numbers with positive sum of digits.
    pos_sod = [i for i in sod if i > 0]
    return len(pos_sod)