def starts_one_ends(n):
    counts = [0, 0, 0, 0, 0, 0]
    digits = set('123456789')
    
    for i in range(1, n + 1):
        num = 1
        any_set = False
        for j in range(i - 1, -1, -1):
            num = num * 10 + digits.pop() if not any_set else num * 10 + digits.pop()
            any_set = (num == 11 or num == 1)
            counts[i] += any_set
        if i < n:
            counts[i] += any_set
    
    return counts[n]