def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    result = []
    for num in sorted_arr:
        if str(num) in '123456789':
            result.append(getNum(num))
    return result if result else []
def getNum(num):
    return {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}[str(num)]