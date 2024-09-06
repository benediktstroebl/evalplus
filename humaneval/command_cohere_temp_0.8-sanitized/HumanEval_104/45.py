def unique_digits(x):
    odd = [int for int in x if any(int % 2 for int in str(int) if int.isdigit())]
    return sorted(odd)