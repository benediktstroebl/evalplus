def tri(n):
    out = [0,1,3]
    if n>=1:
        for i in range(n):
            if i%2 == 0:
                out.append(1 + (i//2))
            else:
                out.append(out[i-1] + out[i-2] + out[i+1])
        return out