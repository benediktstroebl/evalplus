def by_length(arr):
    sorted_arr = sorted(arr, key = lambda x: 1 if x >= 1 and x <= 9 else float('inf'))
    reverse_sorted_arr = sorted(sorted_arr, reverse = True)
    result = []
    for num in reverse_sorted_arr:
        if str(num) == '1':
            result.append('One')
        elif str(num) == '2':
            result.append('Two')
        elif str(num) == '3':
            result.append('Three')
        elif str(num) == '4':
            result.append('Four')
        elif str(num) == '5':
            result.append('Five')
        elif str(num) == '6':
            result.append('Six')
        elif str(num) == '7':
            result.append('Seven')
        elif str(num) == '8':
            result.append('Eight')
        elif str(num) == '9':
            result.append('Nine')
    return result if result else []