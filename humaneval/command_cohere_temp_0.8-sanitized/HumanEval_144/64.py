def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    reciprocal = numn / denomn
    return round(numx * reciprocal) == int(numx * reciprocal)