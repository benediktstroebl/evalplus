def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    arr_str = ' '.join(str(x) for x in arr)
    # sorting the array in reverse order so that the highest number is at the beginning
    sorted_arr_str = ' '.join(sorted(arr_str.split()))
    # cutting the sorted array at the first space to get the highest number
    max_num = sorted_arr_str.split()[0]
    # cutting the original array at the first space to get the same highest number
    idx = arr_str.index(' ')
    left_arr = [x for x in arr if x != max_num]
    right_arr = [x for x in arr if x == max_num]
    # shifting the right array to the beginning of the left array
    return move_one_ball(left_arr + right_arr) if n - idx - 1 >= 0 else False