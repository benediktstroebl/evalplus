

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    assert type(n) == int and n > 0
    def factorial(n):
        """
        Return the factorial of n.
        """
        assert type(n) == int and n > 0
        if n <= 1:
            return 1
        else:
            return n * factorial(n - 1)

    def binomial_coefficient(n, k):
        """
        Compute the binomial coefficient, which is the number of ways to choose k
        out of n.
        """
        assert type(n) == int and type(k) == int and n >= 0 and k >= 0
        if k > n:
            return 0
        else:
            return factorial(n) // (factorial(n - k) * factorial(k))

    def binomial_coefficient_list(n, k):
        """
        Return a list of the binomial coefficients of all integers from 1 to n.
        """
        assert type(n) == int and n >= 0
        if k > n:
            return []
        else:
            
            if k == 0:
                return [1]
            else:
                return [binomial_coefficient(n, x) for x in range(1, k + 1)]

    def solve_for_k(n, k):
        """
        Given n and k, return the k-th entry in the binomial coefficient list,
        where the 0-th entry is 1, and the list begins with 1.
        """
        assert type(n) == int and type(k) == int and n >= 0 and k >= 0
        return binomial_coefficient_list(n, k)[k - 1]

    def collisons(n: int):
        """
        Return the number of collisions between two cars that are traveling
        opposite directions.
        """
        assert type(n) == int and n > 0
        collision_list = []
        for k in range(n + 1):
            collision_list.append(solve_for_k(n, k))
        return sum(collision_list)

    return collisons(n)
