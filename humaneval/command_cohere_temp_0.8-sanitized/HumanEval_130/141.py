def tri(n):
    result = [0,1,3]
    if n >= 1:
        result += [(1 + n/2) if i % 2 == 0 else sum(result[i-1:i+2]) for i in range(1, n+1)]
    return result[:n+1]