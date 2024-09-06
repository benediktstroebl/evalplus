def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    if numx * denomn == numn * denomx:
        return True
    else: 
        return False