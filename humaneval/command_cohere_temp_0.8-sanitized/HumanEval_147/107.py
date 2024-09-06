def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate max triples
    multiples_of_three = []
    for i in range(n):
        for j in range(i + 1, n):
            curr_sum = a[i] + a[j]
            if curr_sum % 3 == 0:
                multiples_of_three.append((a[i], a[j]))
    
    # Count valid triples
    def is_valid(triplet):
        return triplet[0] + triplet[1] + triplet[2] % 3 == 0
    
    count = sum(1 for i in range(len(multiples_of_three)) 
                for x, y in combinations(multiples_of_three[i], 3) 
                if is_valid(x, y, multiples_of_three[i][0]))
    
    return count