def int_to_mini_roman(n):
    if n < 1000:
        res = []
        for x in range(0, n + 1):
            cur = str(x)
            if cur == '1':
                res.append('i')
            elif cur == '2':
                res.append('ii')
            elif cur == '3':
                res.append('iii')
            elif cur == '4':
                res.append('iv')
            elif cur == '5':
                res.append('v')
            elif cur == '6':
                res.append('vi')
            elif cur == '7':
                res.append('vii')
            elif cur == '8':
                res.append('viii')
            elif cur == '9':
                res.append('ix')
            elif cur == '0':
                res.append('x')
        return ''.join(res)
    else:
        return 'Error'