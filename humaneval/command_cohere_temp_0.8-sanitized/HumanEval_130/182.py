def tri(n):
    out = [0,1,3]
    if len(out) < n + 1:
        if n % 2 == 0:
            out.extend([x + y + z for x in out for y in out for z in out[1:n + 1]])
        else:
            out.extend([x + y + z for x in out[1:] for y in out for z in out])
    return out[:n+1]