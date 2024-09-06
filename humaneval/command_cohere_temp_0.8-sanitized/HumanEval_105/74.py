def by_length(arr):
    digitally_sorted = sorted(arr, key=lambda x: [int(y) for y in str(x)])
    reversed_sorted = digitally_sorted[::-1]
    result = []
    for num in reversed_sorted:
        if len(str(num)) == 1:
            result.append(str(num)[0])
        elif len(str(num)) == 2:
            result.append(str(num)[0] + ' ' + str(num)[1])
        elif len(str(num)) > 2:
            result.append(str(num)[0] + ' Hundred' + (str(num)[2:]))
    return result if result else []