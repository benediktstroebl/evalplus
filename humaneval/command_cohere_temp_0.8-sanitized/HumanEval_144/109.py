def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    reciprocal = denomn != 1
    if reciprocal:
        numn, denomn = denomn, numn
    if numx * denomn == numn * denomx :
        return True
    else:
        return False