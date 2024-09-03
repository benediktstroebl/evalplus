def count_nums(arr):
    # Use sum to get all the digits of each element in the array
    digits = [int(x) for x in arr if x.isdigit()]
    basic_sum(digits)
    return sum(x > 0 for x in basic_sum(digits))