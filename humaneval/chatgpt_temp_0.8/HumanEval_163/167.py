def generate_integers(a, b):
    even_digits = []
    for i in range(a, b+1):
        for digit in str(i):
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))
    return sorted(set(even_digits))
