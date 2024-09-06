def derivative(xs: list) -> list:
    result = [0] * (len(xs) + 1)
    degree = len(xs)
    for i in range(degree):
        result[i+1] = result[i] + xs[i] * i
    return result