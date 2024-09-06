def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    result = []
    for num in sorted_arr:
        if str(num) in '15789':
            result.append(str(num)[0] + 'een')
        elif str(num) in '2345':
            result.append(str(num)[0] + 'w')
        elif str(num) in '6789':
            result.append(str(num)[0] + 'h')
    return result if result else []