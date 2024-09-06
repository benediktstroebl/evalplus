def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    reciprocal = denomx * denomn
    return (numx * numn % reciprocal == 0)