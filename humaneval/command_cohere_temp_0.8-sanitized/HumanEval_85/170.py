def add(lst):
    even_odd = []
    for i, num in enumerate(lst):
        if i % 2 == 1 and num % 2 == 0:
            even_odd.append(num)
    return sum(even_odd)