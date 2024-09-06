def rounded_avg(n, m):
    bin_str = [-1 if i == 0 else str(bin(i))[2:] for i in range(n, m + 1)]
    return '0b' + bin_str.pop(0) if bin_str[0][-1] in '01' else '-1' if bin_str == [] else '0b' + ''.join(bin_str)