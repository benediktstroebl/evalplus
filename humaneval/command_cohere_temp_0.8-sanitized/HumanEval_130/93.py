def tri(n):
    out = [0,1,3]
    if len(out) < n + 1:
        if n % 2 == 0:
            out.extend([n//2 + 1, 0])
        else:
            out.extend([0, out[len(out) - 1] + out[len(out) - 2] + (n + 1)//2])
    return out[:n+1]