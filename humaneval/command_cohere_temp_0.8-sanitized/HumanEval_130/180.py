def tri(n):
    sequence, result = [1, 3], [1]
    
    if n == 0:
        return result
    
    for _ in range(1, n + 1):
        if _ % 2 == 1:
            sequence.append(result[-1] + sequence[-2] + sequence[-3])
        else:
            sequence.append(1 + _ / 2)
        result.append(sequence[-1])
    
    return result