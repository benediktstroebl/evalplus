def tri(n):
    out = [0,1,3]
    if len(out) < n + 1:
        if n % 2 == 0:
            out.extend([1 + n//2] * (n + 1))
        else:
            for i in range(1, n + 1, 2):
                out.append(out[i - 1] + out[i - 2] + out[i])
    return out[:n+1]