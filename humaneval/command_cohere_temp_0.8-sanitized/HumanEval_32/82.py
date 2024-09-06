import math
def poly(xs, x):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    # Check if the list has an even number of coefficients and the highest coefficient is non-zero
    if len(xs) % 2 == 0 and xs[-1] != 0:
        x = float(-xs[-1] / (2 * xs[0]))
        # Starts iteration from a number lower than x
        for i in range(100):
            if poly(xs, x) == 0:
                return x
            x += 1 / i
    else:
        return "The list of coefficients is not suitable for finding a zero point."