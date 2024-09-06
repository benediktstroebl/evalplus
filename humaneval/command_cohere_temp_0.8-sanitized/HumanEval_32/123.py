import math
def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero solution.
    Works only for lists xs with an even number of coefficients 
    and maximum non-zero coefficient.
    """
    def divide(a, b):
        """
        Returns (quotient, remainder) from dividing a by b securely.
        Works for negative numbers.
        """
        if b == 0:
            raise ValueError('Divisor b is zero')
        sign_a = (-1 if a < 0 else 1)
        sign_b = (-1 if b < 0 else 1)
        norm_a = abs(a)
        norm_b = abs(b)
        quotient = 0
        remainder = 0
        while norm_a >= norm_b:
            temp = norm_a % norm_b
            remainder = remainder + (temp * sign_b)
            norm_a = norm_a - temp
            quotient = quotient + (temp * sign_a)
        return quotient * sign_b, remainder * sign_a

    def solve_linear(a, b, x):
        """
        Solves linear equation a*x + b*x = 0.
        """
        _, x = divide(a, b)
        return x

    def solve_quad(a, b, c, d, x):
        """
        Solves quadratic equation a*x^2 + b*x + c = 0.
        """
        if d == 0:  # quadratic equation has multiple solutions, or no solutions
            return []
        _, x = divide(b**2 - 4*a*d, 2*a)
        return [x + d/(2*a) for x in [x - math.sqrt(x*x + 4*a*d), x + math.sqrt(x*x + 4*a*d)]]

    def solve_cubic(a, b, c, d, x):
        """
        Solves cubic equation a*x^3 + b*x^2 + c*x + d = 0.
        """
        if d == 0:  # cubic equation has multiple solutions, or no solutions
            return []
        a = 1/a
        _, x = divide(b*a - 3*c, 3*a)
        return [x + (c + d*a)/(3*a) for x in [x - math.pow(3, 1/3) * math.sqrt(3)*a, x - math.pow(3, 1/3) * -math.sqrt(3)*a, x]]

    def solve_sec_poly(xs, x):
        """
        Solves polynomial equation xs[0]*x^n + xs[1]*x^(n-1) + ... + xs[n-1] = 0.
        """
        n = len(xs)
        for k in range(n, 0, -1):
            if n % k != 0:  # pragma: no cover
                continue