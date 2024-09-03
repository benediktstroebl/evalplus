def tri(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    sequence = [0]
    
    if n % 2 == 0:
        sequence.append(sequence[-1] + sequence[-2])
    else:
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    
    return sequence