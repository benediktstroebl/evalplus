def by_length(arr):
    sized = [x for x in arr if 1 <= x <= 9]
    return [x.split('')[0].translate(str.maketrans('123456789', 'One Two Three Four Five Six Seven Eight Nine')) for x in reversed(sorted(sized))] if sized else []