def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    reciprocal = denomn != 1
    if reciprocal:
        numn, denomn = denomn, numn
    if numx == numn and denomx == denomn:
        return True
    elif numx * denomn == numn * denomx:
        return True
    else:
        return False