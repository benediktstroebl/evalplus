def solve(n):
    """
    :param n: Integer to be transformed to binary string
    :return: Binary string summation of integer
    """
    bin_list = [str(n)]
    while len(bin_list) > 1:
        temp = []
        for i in range(len(bin_list)):
            bi = bin_list.pop(0)
            p = bi.find('1')
            if p == -1:
                temp.append(bi)
                continue
            else:
                carry = int(bi[:p])
                temp.append(str(carry))
                if p < len(bi)-1:
                    bi = bi[p+1:]
                    temp.append(bi)
                else:
                    bi = bi[p+1:]
                    if len(bi) == 1:
                        temp.append('0')
                    temp.append(bi)
        bin_list = temp
    if bin_list[0] == '0':
        bin_list[0] = 'false'
    return bin_list[0]