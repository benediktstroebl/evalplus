def rounded_avg(n, m):
    average = (n + m) // 2
    if n > m:
        return -1
    rounded = bin(round(average)).replace('0b', '').rjust(8, '0')
    return '0b' + rounded if rounded != 'NaN' else '0b1111'